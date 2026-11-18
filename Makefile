COMPOSE = docker compose -f docker-compose.yml

all:
	$(COMPOSE) up -d --build

up:
	$(COMPOSE) up -d

start:
	$(COMPOSE) start

stop:
	$(COMPOSE) stop

down:
	$(COMPOSE) down

logs:
	$(COMPOSE) logs