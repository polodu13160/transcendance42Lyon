// SPDX-License-Identifier: MIT
pragma solidity ^0.8.22;

import {Test, console} from "forge-std/Test.sol";
import {TournamentScores} from "../src/TournamentScores.sol";

contract TournamentScoresTest is Test {
	TournamentScores public tournamentscores;
	address public backend;
	address public lucas;
	address public bad_addr;

	function setUp() public {
		backend = makeAddr("backend");
		lucas = makeAddr("lucas");
		bad_addr = address(0);
		tournamentscores = new TournamentScores(backend);
	}
		// vm.expectRevert("Unauthorized caller");
		// vm.prank(lucas);
		// tournamentscores.recordScore(1000, lucas, 3500);
		// vm.startPrank(address)
		// vm.stopPrank(address)
		// assertEq(a, b) : a == b
		// vm.expectEmit(Topic1, Topic2, Topic3, Data)  Topic = indexed

	function test_contract_variables() public {
		assertTrue(tournamentscores.authorizedCaller() == backend);
		vm.prank(backend);
		assertEq(tournamentscores.owner(), address(this));
	}

	function test_RecordScore_Success() public {
		vm.expectEmit(true, true, false, true);
		emit TournamentScores.ScoreRecorded(1, lucas, 5, block.timestamp);
		vm.prank(backend);
		tournamentscores.recordScore(1, lucas, 5);
		assertEq(tournamentscores.getScores(1).length, 1);
		assertEq(tournamentscores.getScores(1)[0].player, lucas);
		assertEq(tournamentscores.getScores(1)[0].card_count, 5);
		assertEq(tournamentscores.getScores(1)[0].timestamp, block.timestamp);
	}

	function test_RecordScore_Failure() public {
		vm.expectRevert("Unauthorized caller");
		vm.prank(lucas);
		tournamentscores.recordScore(1, lucas, 350);
	}

	function test_SetAuthorizedCaller_Success() public {
		tournamentscores.setAuthorizedCaller(lucas);
		vm.prank(lucas);
		tournamentscores.recordScore(1, lucas, 3500);
		assertEq(tournamentscores.getScores(1)[0].player, lucas);
		assertEq(tournamentscores.getScores(1)[0].card_count, 3500);
	}

	function test_SetAuthorizedCaller_Failure() public {
		vm.expectRevert();
		vm.prank(lucas);
		tournamentscores.setAuthorizedCaller(lucas);
	}

	function test_BadAdress() public {
		vm.expectRevert("Invalid address for setAuthorizedCaller function");
		tournamentscores.setAuthorizedCaller(bad_addr);
	}
}
