use crate::config::Config;
use anyhow::{Context, Result};
use alloy::primitives::{Address, B256, U256};
use alloy::signers::local::PrivateKeySigner;
use alloy::network::EthereumWallet;
use alloy::providers::{ProviderBuilder};
use alloy::sol;

sol! {
	#[sol(rpc)]
	contract TournamentScoresContract {
		function recordScore(uint256 tournamentId, address player, uint32 cardCount) external;
	}
}

pub async fn send_record_score(config: &Config, tournament_id: u64, player: Address, card_count: u32) ->Result<B256> {
	let signer = config.backend_private_key.parse::<PrivateKeySigner>().context("Invalid backend private key")?;
	let wallet = EthereumWallet::new(signer);
	let rpc_url = config.rpc_http_url.parse().context("Wrong http url format")?;
	let provider = ProviderBuilder::new().wallet(wallet).connect_http(rpc_url);
	let contract = TournamentScoresContract::new(config.lb_contract_address, provider);
	let pending_tx = contract.recordScore(U256::from(tournament_id), player, card_count).send().await.context("Failed to send recordScore transaction")?;
	let receipt = pending_tx.get_receipt().await.context("Failed to get recordScore transaction receipt")?;
	Ok(receipt.transaction_hash)
}
