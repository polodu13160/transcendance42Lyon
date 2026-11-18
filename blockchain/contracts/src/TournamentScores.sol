// SPDX-License-identifier: MIT
pragma solidity ^0.8.20;

import {Ownable} from "lib/openzeppelin-contracts/contracts/access/Ownable.sol";

contract scoreContract is Ownable {
	constructor(address firstCaller) Ownable(msg.sender) {
		authorizedCaller = firstCaller;
	}

	function setAuthorizedCaller(address newCaller) onlyOwner external {
		require(newCaller != address(0), "Invalid address");
		authorizedCaller = newCaller;
	}

	function recordScore(uint256 tournamentId, address player, uint32 cardCount) onlyAuthorized() external {

	}

	function getScores(uint256 tournamentId) external view returns (Score[] memory){

	}

	modifier onlyAuthorized() {

	}

	struct Score {
		address	player;
		uint32	card_count;
		uint64	timestamp;
	}


	address public authorizedCaller;


}


