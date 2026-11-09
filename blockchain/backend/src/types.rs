use alloy::primitives::Address;
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TournamentScore {
	tournament_id : u64,
	player : Address,
	card_count : u64,
	timestamp : u64,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum BlockchainEvent {
	ScoreRecorded(TournamentScore),
}
