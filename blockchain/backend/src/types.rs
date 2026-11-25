use alloy::primitives::{Address, U256};
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TournamentScore {
	pub tournament_id : u64,
	pub player : Address,
	pub card_count : u64,
	pub timestamp : u64,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum BlockchainEvent {
	ScoreRecorded(TournamentScore),
}

#[derive(Deserialize)]
pub struct RecordScoreRequest {
	pub tournament_id: u64,
	pub player: Address,
	pub card_count: u32,
}

#[derive(Deserialize)]
pub struct MintRequest {
	pub player: Address,
	pub amount: U256,
}

#[derive(Deserialize)]
pub struct BurnRequest {
	pub tx_hash: B256,
	pub player: Address,
	pub amount: U256,
}
