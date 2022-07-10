from brownie import accounts, config, SimpleStorage, network
import os


def deploy_simple_storage():
    # account = accounts[0]  # default brownie ganache account
    # account = accounts.load("dev") # my metamask save in brownie
    # account = accounts.add(config["wallets"]["from_key"]) # from config file
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print("Initial value: ", stored_value)
    print("storing value....")
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print("Updated value: ", updated_stored_value)


def get_account():
    if network.show_active() == "developement":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
