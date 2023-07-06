import sys

sys.path.insert(0, ".")

from eth_account import Account
from web3 import Web3

from lantern3 import Lantern3, FlashbotsBuilder, Builder

if len(sys.argv) < 2:
    print("Please provide the private key as an argument.")
    sys.exit()

private_key = sys.argv[1]

w3 = Web3(Web3.HTTPProvider("https://ethereum.publicnode.com"))
l3 = Lantern3(w3)

flashbots_signer = Account.create()
l3.add_builder(FlashbotsBuilder("https://relay.flashbots.net", flashbots_signer))
l3.add_builder(Builder("https://builder0x69.io"))
l3.add_builder(Builder("https://rpc.beaverbuild.org"))
l3.add_builder(Builder("https://rsync-builder.xyz"))

account = w3.eth.account.from_key(private_key)
nonce = w3.eth.get_transaction_count(account.address)
tx = {
    "to": "0x0000000000000000000000000000000000000000",
    "type": 2,
    "maxFeePerGas": 25000000000,  # 25 gwei
    "maxPriorityFeePerGas": 5000000000,  # 5 gwei
    "data": "0x",
    "chainId": 1,
    "value": 1,
    "nonce": nonce,
    "gas": 21000,
}
signed_tx = w3.eth.account.sign_transaction(tx, account.key)

tx["nonce"] += 1
signed_tx2 = w3.eth.account.sign_transaction(tx, account.key)

bundle = [signed_tx, signed_tx2]
print(f"Bundle: [{signed_tx.hash.hex()}, {signed_tx2.hash.hex()}]")

block_number = w3.eth.block_number
max_block_number = block_number + 25
print(f"Request a bundle inclusion by the block #{max_block_number}")
included = l3.send_bundle_and_wait(bundle, max_block_number)
if included != 0:
    print(f"The bundle has been included in the block #{included}")
else:
    print("The bundle has been failed to be included")
