from web3 import Web3
from web3.middleware import geth_poa_middleware
import config


w3 = Web3(Web3.HTTPProvider(config.PROJECT_RINKEBY_ENDPOINT))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
contract = w3.eth.contract(
    address=config.CONTRACT_ADDRESS,
    abi=config.CONTRACT_ABI
)
