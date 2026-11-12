import asyncio
import random
import time
from typing import Literal

from fastapi import FastAPI, Request
from prometheus_client import Counter, Histogram, make_asgi_app, Gauge

app = FastAPI()

# Expose les métriques sur /metrics (Prometheus viendra les scraper ici)
app.mount("/metrics", make_asgi_app())

# --- Métriques ---
GAMES_PLAYED = Counter("games_played", "Nombre de parties jouées", ["mode"])

REQUESTS = Counter(
    "http_requests_total", "Requêtes HTTP", ["method", "route", "status"]
)
LATENCY = Histogram(
    "http_request_duration_seconds",
    "Durée des requêtes HTTP",
    ["method", "route"],
    buckets=(0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5),
)

CONNECTED_PLAYERS = Gauge("connected_players", "Nombre de joueur connecté")

MATCHMAKING = Histogram(
    "matchmaking_duration_seconds",
    "Temps du matchmaking",
    buckets=(0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5),
)

# --- Middleware : s'exécute autour de CHAQUE requête ---
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    duration = time.perf_counter() - start

    route = request.scope.get("route")
    route_label = route.path if route else "unmatched"

    REQUESTS.labels(request.method, route_label, str(response.status_code)).inc()
    LATENCY.labels(request.method, route_label).observe(duration)
    return response


# --- Routes ---
@app.get("/")
async def root():
    return {"status": "ok"}


@app.get("/games/{game_id}")
async def get_game(game_id: int):
    await asyncio.sleep(random.uniform(0.01, 0.3))  # simule de la latence
    return {"game_id": game_id, "state": "fake"}


@app.post("/games")
async def create_game(mode: Literal["solo", "multi"] = "solo"):
    GAMES_PLAYED.labels(mode=mode).inc()
    return {"created": True, "mode": mode}

@app.post("/join")
async def get_connected():
    CONNECTED_PLAYERS.inc()
    return {"status": "joined"}

@app.post("/leave")
async def get_disconnected():
    CONNECTED_PLAYERS.dec()
    return {"status": "left"}

@app.post("/matchmaking")
async def matchmaking():
    with MATCHMAKING.time():  # mesure la durée du bloc et l'enregistre
        await asyncio.sleep(random.uniform(0.05, 2))  # simule la recherche d'un adversaire
    return {"status": "match found"}