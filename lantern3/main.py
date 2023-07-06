import time
from eth_account.datastructures import SignedTransaction
from threading import Thread
from web3 import Web3
from web3.types import BlockData

from lantern3.builder import Builder


class Lantern3:
    """
    High-level interface for sending bundles.

    This class provides a high-level interface for sending bundled transactions
    to multiple block builders, aiming to increase the success rate of inclusion
    in the Ethereum blockchain.

    Expectations:
        - Prevent reverted transactions
        - Prevent front-running, back-running, sandwich attacks

    Requirements:
        - Bundle should consume at least 42000 gas: To mitigate potential issues
          and ensure inclusion, the bundled transactions should consume a
          minimum of 42000 gas
        - Bundle should set a higher gas price than the tail of the block: To
          incentivize miners to include the bundle, a higher gas price than the
          tail of the block should be set.
        - Refer to the Flashbots documentation for details:
          https://docs.flashbots.net/flashbots-auction/searchers/advanced/bundle-pricing#why-arent-my-bundles-being-included

    Args:
        - w3 (Web3): The Web3 instance to interact with the Ethereum network.
        - wait_interval_secs (float, optional): The interval between checking
          for bundle inclusion. Defaults to 1.0 second.
    """

    def __init__(self, w3: Web3, wait_interval_secs: float = 1.0):
        self.w3 = w3
        self.wait_interval_secs = wait_interval_secs
        self.builders: list[Builder] = []

    def add_builder(self, builder: Builder):
        """
        Adds a block builder to the list of builders used by Lantern3.

        Args:
            - builder (Builder): The block builder instance to be added.
        """
        self.builders.append(builder)

    def send_bundle_and_wait(
        self, bundle: list[SignedTransaction], max_block_number: int
    ) -> int:
        """
        Sends the bundled transactions and waits for their inclusion in a block.

        This method sends the bundled transactions to the configured block
        builders and waits for the bundle to be included in a block. It
        continuously checks the latest blocks until the bundle is found or the
        maximum block number is reached.

        Args:
            - bundle (List[SignedTransaction]): The list of signed transactions
              to be bundled and sent.
            - max_block_number (int): The maximum block number to send and check
              for bundle inclusion.

        Returns:
            - int: The block number if the bundle is included in a block;
            otherwise, 0.
        """
        current_block_number = self.w3.eth.block_number
        txs = [signed_tx.rawTransaction.hex() for signed_tx in bundle]
        request_threads = [
            Thread(target=builder.send_bundle, args=(txs, block_number))
            for block_number in range(current_block_number + 1, max_block_number + 1)
            for builder in self.builders
        ]
        for request_thread in request_threads:
            request_thread.start()

        checked_block_number = current_block_number
        while True:
            block = self.w3.eth.get_block("latest")
            current_block_number = block["number"]  # type: ignore
            if self._is_bundle_included(block, bundle):
                return current_block_number
            if current_block_number > checked_block_number + 1:
                for block_number in range(
                    checked_block_number + 1, current_block_number
                ):
                    block = self.w3.eth.get_block(block_number)
                    if self._is_bundle_included(block, bundle):
                        return block_number
            checked_block_number = current_block_number
            if checked_block_number >= max_block_number:
                break
            time.sleep(self.wait_interval_secs)
        return 0

    def _is_bundle_included(
        self, block: BlockData, bundle: list[SignedTransaction]
    ) -> bool:
        tx_hashes_in_block = [tx.hex() for tx in block["transactions"]]  # type: ignore
        return all(signed_tx.hash.hex() in tx_hashes_in_block for signed_tx in bundle)
