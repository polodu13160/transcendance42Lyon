use crate::types::TournamentScore;
use crate::config::Config;
use std::sync::Arc;
use tokio::sync::RwLock;
use crate::types::BlockchainEvent;
use tokio::sync::broadcast;
use axum::extract::State;
use axum::Json;
use axum::extract::ws::WebSocket;
use axum::extract::ws::WebSocketUpgrade;
use axum::response::IntoResponse;
use axum::extract::ws::Message;
use tokio::net::TcpListener;
use axum::{routing::get, Router};
use tower_http::cors::CorsLayer;

#[derive(Clone)]
pub struct SharedScores {
	pub scores: Arc<RwLock<Vec<TournamentScore>>>,
	pub transmitter: broadcast::Sender<BlockchainEvent>,
}

pub async fn get_leaderboard(State(state): State<SharedScores>) -> Json<Vec<TournamentScore>> {
	let scores = state.scores.read().await;
	Json(scores.clone())
}

pub async fn ws_handler(ws: WebSocketUpgrade, State(scores): State<SharedScores>) -> impl IntoResponse {
	ws.on_upgrade(|socket| handle_socket(socket, scores))
}

pub async fn handle_socket(mut socket: WebSocket, scores: SharedScores) {
	let mut receiver = scores.transmitter.subscribe();
	while let Ok(event) = receiver.recv().await {
		if let Ok(event_str) = serde_json::to_string(&event) {
			let msg = Message::Text((event_str).into());
			if socket.send(msg).await.is_err() {
				break;
			}
		}
	}
	eprintln!("Failed to connect receiver to transmitter in Event's WebSocket");
}

pub async fn start_server(config: &Config, scores: SharedScores) -> anyhow::Result<()> {
	let app = Router::new()
	.route("/api/leaderboard", get(get_leaderboard))
	.route("/ws", get(ws_handler))
	.layer(CorsLayer::permissive())
	.with_state(scores);
	let addr = format!("0.0.0.0:{}", config.server_port);
	let listener = TcpListener::bind(&addr).await?;
	println!("HTTP serv and wsocket launched on {}", addr);
	axum::serve(listener, app).await?;
	Ok(())
}
