#!/usr/bin/python3
from brownie import D31eg4t3
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()

    delegate = D31eg4t3.deploy({"from": owner})
    
    print(f"Contract Deployed to {delegate.address}")
    return delegate, owner


def main():
    deploy()
