// SPDX-License-Identifier: MIT
pragma solidity ^0.8.22;

import {Test, console} from "forge-std/Test.sol";
import {MyTestToken} from "../src/MyTestToken.sol";

contract MyTestTokenTest is Test {
	MyTestToken public tokentest;
	address public backend;
	address public lucas;
	address public bad_addr;

	function setUp() public {
		backend = makeAddr("backend");
		lucas = makeAddr("lucas");
		bad_addr = address(0);
		tokentest = new MyTestToken();
	}

	function test_Main_Data() public view {
		assertEq(tokentest.name(), "TestGatchaGameCoin");
		assertEq(tokentest.symbol(), "TGGC");
		assertEq(tokentest.balanceOf(address(this)), 1_000_000 * 10 ** tokentest.decimals());
		assertEq(tokentest.totalSupply(), 1_000_000 * 10 ** tokentest.decimals());
	}

	function test_Mint_Success() public {
		tokentest.mint(lucas, 100 * 10 ** tokentest.decimals());
		assertEq(tokentest.balanceOf(lucas), 100 * 10 ** 18);
		assertEq(tokentest.totalSupply(), 1_000_100 * 10 ** 18);
	}

	function test_Mint_Failure() public {
		vm.expectRevert();
		vm.prank(lucas);
		tokentest.mint(lucas, 2_000_000 * 10 ** 18);
	}

	function test_Burn_Success() public {
		tokentest.mint(lucas, 10 * 10 ** 18);
		vm.prank(lucas);
		tokentest.burn(10 * 10 ** 18);
		assertEq(tokentest.balanceOf(lucas), 0);
	}

	function test_Burn_Failure() public {
		vm.expectRevert();
		vm.prank(lucas);
		tokentest.burn(100 * 10 ** 18);
	}

	function test_Bad_Address() public {
		vm.expectRevert();
		tokentest.mint(bad_addr, 100 * 10 ** 18);
	}
}
