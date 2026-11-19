// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {Test, console} from "forge-std/Test.sol";
import {TournamentScores} from "../src/TournamentScores.sol";

contract TournamentScoresTest is Test {
	TournamentScores public tournamentscores;
	address public backend;
	address public lucas;
	address public bad_user;

	function setUp() public {
		backend = makeAddr("backend");
		lucas = makeAddr("lucas");
		bad_user = makeAddr("baduser");
		tournamentscores = new TournamentScores(backend);
	}
		// vm.expectRevert("Unauthorized caller");
		// vm.prank(lucas);
		// tournamentscores.recordScore(1000, lucas, 3500);
		// vm.startPrank(address)
		// vm.stopPrank(address)
		// asserEq(a, b) : a == b
		// vm.expectEmit(Topic1, Topic2, Topic3, Data)  Topic = indexed

	function test_contract_variables() public {

	}

	function test_RecordScore_Success() public {

	}

	function test_RecordScore_Failure() public {

	}

	function test_SetAuthorizedCaller_Success() public {

	}

	function test_SetAuthorizedCaller_Failure() public {

	}
}
