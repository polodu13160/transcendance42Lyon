# Monitoring (Prometheus, Grafana, Alertmanager)

## Requirements

Docker, Docker Compose and `make`.

## First start

1. Create the `.env` file from the example:

   ```bash
   cp .env.example .env
   ```

   Replace the values with a real username and a real password
   (not `admin`). This file must never be committed.

2. Create the Discord webhook file (secret, ignored by git):

   ```bash
   cp alertmanager/discord_webhook.example alertmanager/discord_webhook
   ```

   Paste the webhook URL of the team's Discord channel into it
   (ask `<contact person>` for it).

3. Start the stack:

   ```bash
   make monitoring-up
   ```

4. Check that it works: in Prometheus, **Status → Targets** should show
   all targets as `UP`.

## Commands

| Command                | Effect            |
|------------------------|-------------------|
| `make monitoring-up`   | Starts the stack  |
| `make monitoring-down` | Stops it          |
| `make monitoring-logs` | Shows the logs    |

## Access

Ports are only exposed on the local machine.

| Service      | URL                   | Login                  |
|--------------|-----------------------|------------------------|
| Grafana      | http://localhost:3000 | credentials from `.env` |
| Prometheus   | http://localhost:9090 | none                   |
| Alertmanager | http://localhost:9093 | none                   |

## How it works

- The datasource and the dashboard are loaded automatically at startup
  from `grafana/provisioning/` and `grafana/dashboards/infra.json`.
- To change the dashboard: edit it in Grafana, export it as JSON
  (Classic format), then replace `grafana/dashboards/infra.json`.
- Data is stored in `prom_data/` and `graf_data/` (not versioned).

## Alerts

- Rules are defined in `prometheus/alerts.yml`. For now there is only one:
  `TargetDown` fires when a service has been unreachable for 1 minute.
- Routing and receivers are defined in `alertmanager/alertmanager.yml`.
  Alerts are sent to a Discord channel.
- More alerts will be added over time.

## Coming next

- Connect the API once it is ready (`backend` job in `prometheus.yml`).
- Business dashboards.