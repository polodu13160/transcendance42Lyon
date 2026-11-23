use alloy::primitives::Address;
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
	tournament_id: u64,
	player: Address,
	card_count: u32,
}
