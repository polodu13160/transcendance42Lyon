use crate::config::Config;
use crate::types::BlockchainEvent;
use crate::types::TournamentScore;
use std::time::Duration;
use tokio::time::sleep;
use alloy::providers::{Provider, ProviderBuilder};
use alloy::rpc::client::WsConnect;
use tokio_stream::StreamExt;
use tokio::sync::broadcast;
use alloy::rpc::types::eth::Filter;
use anyhow::Result;
use alloy::sol;
use std::sync::Arc;
use tokio::sync::RwLock;

sol! {
	#[derive(Debug)]
	event ScoreRecorded (
		uint256 indexed tournament_id,
		address indexed player,
		uint256 card_count,
		uint256 timestamp,
	);
}

pub async fn listener(config: Config, transmitter: broadcast::Sender<BlockchainEvent>, scores: Arc<RwLock<Vec<TournamentScore>>>) -> Result<()> {
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
							scores.write().await.push(score.clone());
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
