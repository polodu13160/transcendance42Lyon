// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {Ownable} from "lib/openzeppelin-contracts/contracts/access/Ownable.sol";
import {ERC20} from "lib/openzeppelin-contracts/contracts/token/ERC20/ERC20.sol";

contract MyTestToken is ERC20, Ownable {
	constructor() ERC20("TestGatchaGameCoin", "TGGC") Ownable(msg.sender) {
		_mint(msg.sender, 1_000_000 * 10 ** decimals());
	}

	function mint(address _to, uint256 _amount) external onlyOwner {
		_mint(_to, _amount);
	}

	function burn(uint256 _amount) external {
		_burn(msg.sender, _amount);
	}
}
