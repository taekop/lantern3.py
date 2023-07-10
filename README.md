# lantern3.py

Light up the Ethereum blockchain with Lantern3, a Python library that provides high-level interfaces for sending bundled transactions to block builders. Lantern3 aims to increase the success rate of transaction inclusion while mitigating issues such as transaction reverts, front-running, back-running, and sandwich attacks.

## Builders

Lantern3 supports multiple block builders that you can use to send your bundled transactions.

| Name         | RPC Endpoint                             | Website                                                       | Notes                                               |
| ------------ | ---------------------------------------- | ------------------------------------------------------------- | --------------------------------------------------- |
| Builder0x69  | `https://builder0x69.io`                 | [@builder0x69](https://twitter.com/builder0x69)               |                                                     |
| Beaverbuild  | `https://rpc.beaverbuild.org`            | [beaverbuild.org](https://beaverbuild.org/)                   |                                                     |
| Flashbots    | `https://relay.flashbots.net`            | [flashbots.net](https://flashbots.net)                        | [`FlashbotsBuilder`](lantern3/builder/flashbots.py) |
| Rsync        | `https://rsync-builder.xyz`              | [rsync-builder.xyz](https://rsync-builder.xyz/)               |                                                     |
| Blocknative  | `https://api.blocknative.com/v1/auction` | [blocknative.com](https://www.blocknative.com/)               |                                                     |
| Gambit Labs  | `https://builder.gmbit.co/rpc`           | [gmbit.co](https://www.gmbit.co/)                             |                                                     |
| Eth-Builder  | `https://eth-builder.com`                | [eth-builder.com](https://eth-builder.com/)                   |                                                     |
| Titan        | `https://rpc.titanbuilder.xyz`           | [titanbuilder.xyz](https://www.titanbuilder.xyz/)             |                                                     |
| BuildAI      | `https://buildai.net`                    | [buildai.net](https://buildai.net/)                           |                                                     |
| Payload      | `https://rpc.payload.de`                 | [payload.de](https://payload.de/)                             |                                                     |
| Bloxroute    | `https://mev.api.blxrbdn.com`            | [bloxroute.com](https://bloxroute.com/)                       |                                                     |
| Lightspeed   | `https://rpc.lightspeedbuilder.info`     | [lightspeedbuilder.info](https://www.lightspeedbuilder.info/) |                                                     |
| nfactorial   | `https://rpc.nfactorial.xyz`             | [nfactorial.xyz](https://nfactorial.xyz/)                     |                                                     |
| Boba-Builder | `https://boba-builder.com/searcher`      | [boba-builder.com](http://boba-builder.com/)                  |                                                     |
| f1b.io       | `https://rpc.f1b.io`                     | [f1b.io](https://f1b.io/)                                     |                                                     |



Please refer to the documentation of each block builder for any specific requirements or considerations when using them.

## Examples

To get started with Lantern3, you can explore the provided examples. The following example demonstrates a simple transfer of Ether:

```shell
$ python3 examples/simple_transfer.py <YOUR_PRIVATE_KEY>
```

Please note that before running the examples, you may need to install the necessary dependencies by following the installation instructions in the project's documentation.

## Contributing

We welcome contributions to Lantern3! If you encounter any issues, have suggestions, or want to contribute improvements or new features, please open an issue or submit a pull request on the GitHub repository.

## License

Lantern3 is licensed under the [MIT License](https://opensource.org/license/mit/). See the [LICENSE](LICENSE) file for more details.
