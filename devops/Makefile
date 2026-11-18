COMPOSE = docker compose -f docker-compose.yml

all:
	$(COMPOSE) up -d --build

monitoring-up:
	$(COMPOSE) up -d

monitoring-start:
	$(COMPOSE) start

monitoring-stop:
	$(COMPOSE) stop

monitoring-down:
	$(COMPOSE) down

monitoring-logs:
	$(COMPOSE) logs