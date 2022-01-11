from web3 import Web3
import json
import os 

def create_contract_class(abi_filename: str):
    with open(abi_filename, 'r') as file_reader:
        contract_data = json.loads(file_reader.read())
    abi = contract_data['abi']
    GreeterContract = infura_w3.eth.contract(abi=abi)
    return GreeterContract

def create_greeter_contract():
    contract = create_contract_class('Greeter_ABI.json')(
        address='0xE2f6779E9cEa809a69b12772116618816F628EfC')
    return contract


infura_w3 = Web3(
    Web3.HTTPProvider(
        f'https://ropsten.infura.io/v3/{os.environ["INFURA_KEY"]}'))
local_w3 = Web3(Web3.IPCProvider())

contract = create_greeter_contract()
print(contract.functions.greet().call())
