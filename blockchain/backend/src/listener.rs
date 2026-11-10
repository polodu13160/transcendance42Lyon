mod config;
use config::Config;
use std::time::Duration::from_secs;
use tokio::time::sleep;
use alloy::providers::{WSconnect, Provider, ProviderBuilder};

pub async fn listener(config: Config, transmitter: broadcast::Sender<BlockchainEvent>) -> Result<()> {
	let wsocket = WSconnect::new(config.rpc_ws_url);
	let delay = Duration::from_secs(1);
	loop {
		match ProviderBuilder::new().connect_ws(wsocket).await {
			Ok(provider) => {
				delay = Duration::from_secs(1);
				while let Some(logs) = stream.next().await {

				}
				// erreur de co si on sort du while
			}
			Err(e) => {
				eprintln!("Lost connexion to websocket, try to reconnect in {} seconds", delay);
				tokio::time::sleep(delay).await;
				delay *= 2;
				if delay > Duration::from_secs(30) {
					delay = 30;
				}
			}
		}

	}
	transmitter.subscribe()
}
