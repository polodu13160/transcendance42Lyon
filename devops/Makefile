COMPOSE = docker compose -f docker-compose.yml

all:
	$(COMPOSE) up -d --build

up:
	$(COMPOSE) up -d

start:
	$(COMPOSE) start

stop:
	$(COMPOSE) stop

build:
	$(COMPOSE) up --build -d

down:
	$(COMPOSE) down

logs:
	$(COMPOSE) logs