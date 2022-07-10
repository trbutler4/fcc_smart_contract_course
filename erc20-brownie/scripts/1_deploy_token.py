from brownie import MyToken, accounts
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")

def main():
    account = accounts[0]
    my_token = MyToken.deploy(initial_supply, {"from": account})
    print(my_token.name())
