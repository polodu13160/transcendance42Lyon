// SPDX-License-identifier: MIT
pragma solidity ^0.8.20;

import {Ownable} from "lib/openzeppelin-contracts/contracts/access/Ownable.sol";

contract ScoreContract is Ownable {
	struct Score {
		address	player;
		uint32	card_count;
		uint64	timestamp;
	}

	mapping(uint256 => Score[]) private _tournamentScores;
	address public authorizedCaller;

	event ScoreRecorded(
		uint256 indexed tournament_id,
		address indexed player,
		uint256 card_count,
		uint256 timestamp
	);

	constructor(address firstCaller) Ownable(msg.sender) {
		authorizedCaller = firstCaller;
	}

	function setAuthorizedCaller(address newCaller) external onlyOwner {
		require(newCaller != address(0), "Invalid address");
		authorizedCaller = newCaller;
	}

	function recordScore(uint256 tournamentId, address player, uint32 cardCount) external onlyAuthorized() {
		_tournamentScores[tournamentId].push(
			Score({
				player: player,
				card_count: cardCount,
				timestamp: uint64(block.timestamp)
			})
		);
		emit ScoreRecorded(tournamentId, player, cardCount, block.timestamp);
	}

	function getScores(uint256 tournamentId) external view returns (Score[] memory){
		return _tournamentScores[tournamentId];
	}

	modifier onlyAuthorized() {
		require(msg.sender == authorizedCaller, "Unauthorized caller");
		_;
	}
}


