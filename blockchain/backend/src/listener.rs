use crate::config::Config;
use crate::types::BlockchainEvent;
use crate::types::TournamentScore;
use alloy::providers::{Provider, ProviderBuilder};
use alloy::rpc::{client::WsConnect, types::eth::Filter};
use alloy::sol;
use anyhow::Result;
use std::time::Duration;
use std::sync::Arc;
use tokio::sync::{broadcast, RwLock};
use tokio::time::sleep;
use tokio_stream::StreamExt;

sol! {
	#[derive(Debug)]
	event ScoreRecorded (
		uint256 indexed tournament_id,
		address indexed player,
		uint256 card_count,
		uint256 timestamp,
	);
}

pub async fn listener(config: Arc<Config>, transmitter: broadcast::Sender<BlockchainEvent>, scores: Arc<RwLock<Vec<TournamentScore>>>) -> Result<()> {
	let mut delay = Duration::from_secs(1);
	let filter = Filter::new().address(config.contract_address);
	loop {
		let wsocket = WsConnect::new(config.rpc_ws_url.clone());
		match ProviderBuilder::new().connect_ws(wsocket).await {
			Ok(provider) => {
				delay = Duration::from_secs(1);
				if let Ok(sub_log) = provider.subscribe_logs(&filter).await {
					let mut stream = sub_log.into_stream();
					while let Some(logs) = stream.next().await {
						if let Ok(decoded) = logs.log_decode::<ScoreRecorded>() {
							let event = decoded.data();
							let score = TournamentScore {
								tournament_id: event.tournament_id.to::<u64>(),
								player: event.player,
								card_count: event.card_count.to::<u64>(),
								timestamp: event.timestamp.to::<u64>(),
							};
							let mut scores_vec = scores.write().await;
							if let Some(existing_score) = scores_vec.iter_mut().find(|u| u.player == score.player && u.tournament_id == score.tournament_id) {
								existing_score.card_count = score.card_count;
								existing_score.timestamp = score.timestamp;
							}
							else {
								scores_vec.push(score.clone());
							}
							let _ = transmitter.send(BlockchainEvent::ScoreRecorded(score));
						}
					}
				}
				// erreur de co si on sort du while
				eprintln!("Lost connexion to websocket");
			}
			Err(e) => {
				eprintln!("Failed to connect to websocket {e}, try to reconnect in {} seconds", delay.as_secs());
			}
		}
		sleep(delay).await;
		delay *= 2;
		if delay > Duration::from_secs(30) {
			delay = Duration::from_secs(30);
		}
	}
}
