use alloy::primitives::Address;
use anyhow::{Context, Result};
use dotenvy::dotenv;
use std::env;

#[derive(Clone)]
pub struct Config {
	pub rpc_ws_url : String,
	pub rpc_http_url : String,
	pub lb_contract_address : Address,
	pub token_contract_address: Address,
	pub server_port : u16,
	pub backend_private_key : String,
}

impl Config {
	pub fn load() -> Result<Self> {
		dotenv().ok();
		let rpc_ws_url = env::var("RPC_WS_URL").context("Env var RPC_WS_URL not found")?;
		let rpc_http_url = env::var("RPC_HTTP_URL").context("Env var RPC_HTTP_URL not found")?;
		let lb_contract_address = env::var("LEADERBOARD_CONTRACT_ADDRESS").context("Env var LEADERBOARD_CONTRACT_ADDRESS not found")?.parse::<Address>().context("Invalid format for LEADERBOARD_CONTRACT_ADDRESS")?;
		let token_contract_address = env::var("TOKEN_CONTRACT_ADDRESS").context("Env var TOKEN_CONTRACT_ADDRESS not found")?.parse::<Address>().context("Invalid format for TOKEN_CONTRACT_ADDRESS")?;
		let server_port = env::var("SERVER_PORT").context("Env var SERVER_PORT not found")?.parse::<u16>().context("Invalid format for SERVER_PORT")?;
		let backend_private_key = env::var("BACKEND_PRIVATE_KEY").context("Env var BACKEND_PRIVATE_KEY not found")?;
		Ok(Self{
			rpc_ws_url,
			rpc_http_url,
			lb_contract_address,
			token_contract_address,
			server_port,
			backend_private_key,
		})
	}
}
