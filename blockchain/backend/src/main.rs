mod config;
mod types;
mod listener;
mod server;
mod tx_senders;
mod token;
use crate::listener::listener;
use config::Config;
use std::sync::Arc;
use std::collections::HashSet;
use tokio::sync::RwLock;
use tokio::sync::broadcast;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
	let config = Arc::new(Config::load()?);
	println!("ws url : {}", config.rpc_ws_url);
	println!("http url : {}", config.rpc_http_url);
	println!("leaderboard contract addr : {}", config.lb_contract_address);
	println!("token contract addr : {}", config.token_contract_address);
	println!("server port : {}", config.server_port);
	let (transmitter, _receiver) = broadcast::channel(100);
	let initial_scores = tx_senders::get_initial_scores(&config, 1).await.unwrap_or_else(|e| {eprintln!("Warning: failed to get initial scores: {e}"); Vec::new()});
	let scores = Arc::new(RwLock::new(initial_scores));
	let listener_config = config.clone();
	let listener_transmit = transmitter.clone();
	let listener_scores  = scores.clone();
	tokio::spawn(async move {
		if let Err(e) = listener(listener_config, listener_transmit, listener_scores).await {
			eprintln!("Error on listener: {e}");
		}
	});
	let existing_tournaments = Arc::new(RwLock::new(HashSet::new()));
	let state = server::SharedScores {
		scores: scores.clone(),
		config: config.clone(),
		transmitter: transmitter.clone(),
		existing_tournaments: existing_tournaments.clone(),
	};
	server::start_server(&config, state).await?;
	Ok(())
}
