import json
from typing import Any
from eth_account import messages
from eth_account.signers.base import BaseAccount
from web3 import Web3

from lantern3.builder import Builder


class FlashbotsBuilder(Builder):
    """
    Class responsible for sending RPC requests to a Flashbots-compatible block
    builder in Ethereum.

    This class extends the functionality of the Builder class to support
    Flashbots-specific requirements, such as including the X-Flashbots-Signature
    header in the requests.

    Note:
        The signer used in this class is responsible for signing bundles and
        establishing flashbots reputation. It does not sign the individual
        transactions within the bundle. This account should not store funds

    Args:
        url (str): The URL of the Flashbots-compatible block builder.
        signer (BaseAccount): The account used to sign the Flashbots message.
    """

    def __init__(self, url: str, signer: BaseAccount):
        self.url = url
        self.signer = signer
        self.rid = 0

    def _headers(self, body: dict[str, Any]) -> dict[str, str]:
        message = messages.encode_defunct(text=Web3.keccak(text=json.dumps(body)).hex())
        x_flashbots_signature = (
            str(self.signer.address)
            + ":"
            + self.signer.sign_message(message).signature.hex()
        )
        return {
            "accept": "application/json",
            "content-type": "application/json",
            "X-Flashbots-Signature": x_flashbots_signature,
        }
