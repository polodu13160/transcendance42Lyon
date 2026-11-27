use crate::config::Config;
use crate::types::{TournamentScore, BlockchainEvent, RecordScoreRequest, MintRequest, BurnRequest};
use crate::tx_senders::{send_record_score, get_initial_scores};
use crate::token::{get_token_balance, send_mint, check_burn_transaction};
use alloy::primitives::Address;
use axum::http::StatusCode;
use axum::extract::{State, ws::WebSocket, ws::WebSocketUpgrade, Path};
use axum::{Json, Router};
use axum::response::IntoResponse;
use axum::extract::ws::Message;
use axum::routing::{get, post};
use std::sync::Arc;
use std::collections::HashSet;
use tokio::sync::{broadcast, RwLock};
use tokio::net::TcpListener;
use tower_http::cors::CorsLayer;

#[derive(Clone)]
pub struct SharedScores {
	pub scores: Arc<RwLock<Vec<TournamentScore>>>,
	pub config: Arc<Config>,
	pub transmitter: broadcast::Sender<BlockchainEvent>,
	pub existing_tournaments: Arc<RwLock<HashSet<u64>>>,
}

async fn check_existing_score(state: &SharedScores, tournament_id: u64) -> anyhow::Result<()> {
	let read_guard = state.existing_tournaments.read().await;
	if read_guard.contains(&tournament_id) {
		return Ok(());
	}
	drop(read_guard);
	let initial_scores = get_initial_scores(&state.config, tournament_id).await?;
	let mut scores_vec = state.scores.write().await;
	for i in initial_scores {
		if let Some(existing_score) = scores_vec.iter_mut().find(|u| u.player == i.player) {
			existing_score.card_count = i.card_count;
			existing_score.timestamp = i.timestamp;
		}
		else {
			scores_vec.push(i.clone());
		}
	}
	drop(scores_vec);
	let mut scores_set = state.existing_tournaments.write().await;
	scores_set.insert(tournament_id);
	Ok(())
}

pub async fn record_score_handler(State(state): State<SharedScores>, Json(data): Json<RecordScoreRequest>) -> impl IntoResponse {
	let new_total = {
		let read_guard = state.scores.read().await;
		if let Some(existing_score) = read_guard.iter().find(|u| u.player == data.player && u.tournament_id == data.tournament_id) {
			data.card_count + existing_score.card_count as u32
			}
		else {
			data.card_count
			}
	};
	match send_record_score(&state.config, data.tournament_id, data.player, new_total).await {
		Ok(transaction_hash) => {
			(StatusCode::OK, Json(serde_json::json!({ "status": "success", "transaction_hash": format!("{:#x}", transaction_hash) })))
		}
		Err(e) => {
			(StatusCode::INTERNAL_SERVER_ERROR, Json(serde_json::json!({ "error": e.to_string() })))
		}
	}
}

pub async fn get_tournament_leaderboard(State(state): State<SharedScores>, Path(tournament_id): Path<u64>) -> impl IntoResponse {
	match check_existing_score(&state, tournament_id).await {
		Ok(()) => {
			let mut leaderboard: Vec<TournamentScore> = {
				let read_guard = state.scores.read().await;
				read_guard.iter().filter(|s| s.tournament_id == tournament_id).cloned().collect()
			};
			leaderboard.sort_by(|a, b| {
				b.card_count.cmp(&a.card_count).then(a.timestamp.cmp(&b.timestamp))
			});
			(StatusCode::OK, Json(serde_json::json!(leaderboard)))
		}
		Err(e) => {
			(StatusCode::INTERNAL_SERVER_ERROR, Json(serde_json::json!({"error": e.to_string() })))
		}
	}
}

pub async fn get_balance_handler(State(state): State<SharedScores>, Path(player): Path<Address>) -> impl IntoResponse {
	match get_token_balance(&state.config, player).await {
		Ok(balance) => {
			(StatusCode::OK, Json(serde_json::json!({"player": format!("{:#x}", player), "balance": balance.to_string() })))
		}
		Err(e) => {
			(StatusCode::INTERNAL_SERVER_ERROR, Json(serde_json::json!({"error": e.to_string() })))
		}
	}
}

pub async fn mint_handler(State(state): State<SharedScores>, Json(data): Json<MintRequest>) -> impl IntoResponse {
	match send_mint(&state.config, data.player, data.amount).await {
		Ok(transaction_hash) => {
			(StatusCode::OK, Json(serde_json::json!({ "status": "success", "transaction_hash": format!("{:#x}", transaction_hash) })))
		}
		Err(e) => {
			(StatusCode::INTERNAL_SERVER_ERROR, Json(serde_json::json!({ "error": e.to_string() })))
		}
	}
}

pub async fn burn_handler(State(state): State<SharedScores>, Json(data): Json<BurnRequest>) -> impl IntoResponse {
	match check_burn_transaction(&state.config, data.tx_hash, data.player, data.amount).await {
		Ok(true) => {
			(StatusCode::OK, Json(serde_json::json!({ "check": "true" })))
		}
		Ok(false) => {
			(StatusCode::BAD_REQUEST, Json(serde_json::json!({ "check": "false" })))
		}
		Err(e) => {
			(StatusCode::INTERNAL_SERVER_ERROR, Json(serde_json::json!({ "error": e.to_string() })))
		}
	}
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
	.route("/api/scores/record", post(record_score_handler))
	.route("/api/token/balance/{player}", get(get_balance_handler))
	.route("/api/token/mint", post(mint_handler))
	.route("/api/token/burn", post(burn_handler))
	.layer(CorsLayer::permissive())
	.with_state(scores);
	let addr = format!("0.0.0.0:{}", config.server_port);
	let listener = TcpListener::bind(&addr).await?;
	println!("HTTP serv and wsocket launched on {}", addr);
	axum::serve(listener, app).await?;
	Ok(())
}
