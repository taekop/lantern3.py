import requests
from typing import Any


class Builder:
    """
    Class responsible for sending RPC requests to a block builder in Ethereum.

    Note:
        The Builder class is designed to work with the Flashbots RPC endpoint.
        Make sure that the builder follows the specifications mentioned in the
        Flashbots RPC endpoint documentation:
        https://docs.flashbots.net/flashbots-auction/searchers/advanced/rpc-endpoint

    Args:
        url (str): The URL of the Flashbots-compatible block builder.
    """

    def __init__(self, url: str):
        self.url = url
        self.rid = 0

    def _headers(self, _body: dict[str, Any]) -> dict[str, str]:
        return {
            "accept": "application/json",
            "content-type": "application/json",
        }

    def _request(self, method: str, param: dict[str, Any]) -> requests.models.Response:
        self.rid += 1
        body = {
            "id": self.rid,
            "jsonrpc": "2.0",
            "method": method,
            "params": [param],
        }
        headers = self._headers(body)
        return requests.post(self.url, json=body, headers=headers)

    def send_bundle(self, txs: list[str], block_number: int):
        """
        Sends a bundle to the Ethereum block builder.

        Args:
            txs (list): A list of transactions to be included as a bundle.
            block_number (int): The block number to which the bundle should be
            sent.
        """
        param = {"txs": txs, "blockNumber": hex(block_number)}
        response = self._request("eth_sendBundle", param)
        response.raise_for_status()
