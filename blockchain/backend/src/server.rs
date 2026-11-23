use crate::types::TournamentScore;
use crate::config::Config;
use crate::types::BlockchainEvent;
use crate::types::RecordScoreRequest;
use crate::tx_senders::send_record_score;
use axum::http::StatusCode;
use axum::extract::{State, ws::WebSocket, ws::WebSocketUpgrade};
use axum::Json;
use axum::response::IntoResponse;
use axum::extract::ws::Message;
use axum::{routing::get, Router};
use std::sync::Arc;
use tokio::sync::{broadcast, RwLock};
use tokio::net::TcpListener;
use tower_http::cors::CorsLayer;

#[derive(Clone)]
pub struct SharedScores {
	pub scores: Arc<RwLock<Vec<TournamentScore>>>,
	pub config: Arc<Config>,
	pub transmitter: broadcast::Sender<BlockchainEvent>,
}

pub async fn record_score_handler(State(state): State<SharedScores>, Json(data): Json<RecordScoreRequest>) -> impl IntoResponse {
	match send_record_score(&state.config, data.tournament_id, data.player, data.card_count).await {
		Ok(transaction_hash) => {
			(StatusCode::OK, Json(serde_json::json!({ "status": "success", "transaction_hash": format!("{:#x}", transaction_hash) })))
		}
		Err(e) => {
			(StatusCode::INTERNAL_SERVER_ERROR, Json(serde_json::json!({ "error": e.to_string() })))
		}
	}

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
