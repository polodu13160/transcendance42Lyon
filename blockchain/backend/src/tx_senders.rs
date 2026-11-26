use crate::config::Config;
use crate::types::TournamentScore;
use anyhow::{Context, Result};
use alloy::primitives::{Address, B256, U256};
use alloy::signers::local::PrivateKeySigner;
use alloy::network::EthereumWallet;
use alloy::providers::{ProviderBuilder};
use alloy::sol;
use std::collections::HashMap;

sol! {
	#[sol(rpc)]
	contract TournamentScoresContract {
		function recordScore(uint256 tournamentId, address player, uint32 cardCount) external;
		function getScores(uint256 tournamentId) external view returns (Score[] memory);
		struct Score {
			address player;
			uint32 card_count;
			uint64 timestamp;
		}
	}
}

pub async fn get_initial_scores(config: &Config, tournament_id: u64) -> Result<Vec<TournamentScore>> {
	let rpc_url = config.rpc_http_url.parse().context("Wrong http url format")?;
	let provider = ProviderBuilder::new().connect_http(rpc_url);
	let contract = TournamentScoresContract::new(config.lb_contract_address, provider);
	let initial_scores = contract.getScores(U256::from(tournament_id)).call().await?;
	let mut res_score = HashMap::new();
	for i in initial_scores {
		let score = TournamentScore {
			tournament_id: tournament_id,
			player: i.player,
			card_count: i.card_count as u64,
			timestamp: i.timestamp,
		};
		res_score.insert(i.player, score);
	}
	Ok(res_score.into_values().collect())
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
