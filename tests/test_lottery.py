from brownie import Lottery, accounts, network, config
from web3 import Web3


def test_get_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account}
    )
    # these numebrs are based off current ethereum price
    # assert lottery.getEntranceFee() > Web3.toWei(0.010, "ether")
    # assert lottery.getEntranceFee() < Web3.toWei(0.050, "ether")
