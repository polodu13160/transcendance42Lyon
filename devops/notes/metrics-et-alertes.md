# Metrics et alertes à mettre en place — Transcendence

État actuel : `node_exporter` (host), `backend` (prometheus-fastapi-instrumentator sur `/metrics`), Prometheus, Grafana (dashboard *Infra*), Alertmanager → Discord, une seule alerte (`TargetDown`).

Priorités : **P1** = à faire en premier (utile tout de suite / facile), **P2** = important, **P3** = bonus / montre une vraie maîtrise.

---

## 1. Nouveaux exporters / sources de metrics

| Prio | Exporter | Pourquoi | Image |
|---|---|---|---|
| P1 | **cAdvisor** | Metrics *par conteneur* (CPU, RAM, redémarrages). Aujourd'hui on ne voit que l'hôte, et on n'a pas vu le backend en crash-loop. | `gcr.io/cadvisor/cadvisor` |
| P1 | **postgres_exporter** | La BDD est le point central (users, cartes, achats, échanges). | `prometheuscommunity/postgres-exporter` |
| P2 | **nginx-prometheus-exporter** | Connexions actives / requêtes reçues par le reverse proxy. Nécessite `stub_status` dans `nginx.conf` (sur un port interne, pas exposé). | `nginx/nginx-prometheus-exporter` |
| P2 | **blackbox_exporter** | Teste le site *de l'extérieur* comme un utilisateur (front via nginx, `/api/...`), + expiration du certificat TLS si HTTPS. | `prom/blackbox-exporter` |
| P2 | **Metrics métier custom** dans le backend | Voir section 3 — c'est ce qui rend le monitoring spécifique au projet. | `prometheus_client` (déjà installé via l'instrumentator) |
| P3 | **node_exporter textfile collector** | Exposer le résultat des scripts de backup (timestamp du dernier backup réussi, taille). | déjà présent, ajouter `--collector.textfile.directory` |

> Penser à scraper Alertmanager et Grafana eux-mêmes (`alertmanager:9093`, `grafana:3000/metrics`) : ils exposent déjà des metrics.

---

## 2. Metrics techniques à observer

### 2.1 Backend / API (déjà disponibles via l'instrumentator)

Metrics exposées : `http_requests_total{handler,method,status}` (status groupé en `2xx`/`4xx`/`5xx`), `http_request_duration_seconds_bucket{handler,method}`, `http_request_size_bytes`, `http_response_size_bytes`.

- [ ] **P1** Requêtes/s par route
  `sum by (handler) (rate(http_requests_total{handler!="/metrics"}[5m]))`
- [ ] **P1** Taux d'erreurs 5xx (%)
  `100 * sum(rate(http_requests_total{status="5xx"}[5m])) / sum(rate(http_requests_total[5m]))`
- [ ] **P1** Latence p95 / p99 par route
  `histogram_quantile(0.95, sum by (le, handler) (rate(http_request_duration_seconds_bucket[5m])))`
  ⚠️ dans `notes/query.md` la query p95 utilise `prometheus_http_request_duration_seconds_bucket` → c'est la latence de **Prometheus**, pas du backend.
- [ ] **P2** Taux de 4xx par route (un pic de 401/403 = souvent un bug front ou une attaque)
- [ ] **P2** Taille des réponses (détecter une route qui renvoie toute la table `cards`)
- [ ] **P3** Pool de connexions SQLAlchemy : gauge custom `db_pool_checked_out` = `engine.pool.checkedout()`

### 2.2 Conteneurs (cAdvisor)

- [ ] **P1** CPU par conteneur : `sum by (name) (rate(container_cpu_usage_seconds_total{name!=""}[5m]))`
- [ ] **P1** RAM par conteneur : `container_memory_working_set_bytes{name!=""}`
- [ ] **P1** Redémarrage récent : `time() - container_start_time_seconds{name!=""} < 120`
- [ ] **P2** Réseau par conteneur : `rate(container_network_receive_bytes_total[5m])`

### 2.3 PostgreSQL (postgres_exporter)

- [ ] **P1** BDD joignable : `pg_up`
- [ ] **P1** Connexions utilisées vs max :
  `sum(pg_stat_database_numbackends) / max(pg_settings_max_connections) * 100`
- [ ] **P2** Taille de la base : `pg_database_size_bytes{datname="postgre_db"}`
- [ ] **P2** Transactions/s et rollbacks : `rate(pg_stat_database_xact_commit[5m])`, `rate(pg_stat_database_xact_rollback[5m])`
- [ ] **P2** Deadlocks : `increase(pg_stat_database_deadlocks[10m])`
- [ ] **P3** Cache hit ratio : `blks_hit / (blks_hit + blks_read)` (doit rester > 99 %)

### 2.4 Nginx / disponibilité externe

- [ ] **P2** Connexions actives : `nginx_connections_active`
- [ ] **P2** Requêtes/s : `rate(nginx_http_requests_total[5m])`
- [ ] **P2** Le site répond (blackbox) : `probe_success{job="blackbox"}`, temps de réponse `probe_duration_seconds`
- [ ] **P3** Jours avant expiration du certificat : `(probe_ssl_earliest_cert_expiry - time()) / 86400`

### 2.5 Host (déjà en place)

CPU, RAM, disque, réseau → OK. À ajouter :
- [ ] **P2** Prévision disque plein : `predict_linear(node_filesystem_avail_bytes{mountpoint="/"}[6h], 24*3600) < 0`
- [ ] **P3** Load average vs nombre de CPU : `node_load5 / count(node_cpu_seconds_total{mode="idle"})`

---

## 3. Metrics métier (custom, dans le backend)

C'est ce qui différencie un monitoring « générique » d'un monitoring du projet. À déclarer avec `prometheus_client`, elles seront exposées automatiquement sur le même `/metrics`.

```python
# backend/app/core/metrics.py
from prometheus_client import Counter, Gauge, Histogram

LOGIN_ATTEMPTS = Counter("app_login_attempts_total", "Tentatives de login", ["result"])  # success | bad_password | unknown_user
BOOSTERS_OPENED = Counter("app_boosters_opened_total", "Boosters ouverts")
CARDS_DROPPED = Counter("app_cards_dropped_total", "Cartes obtenues", ["rarity", "shiny"])
PURCHASES = Counter("app_purchases_total", "Achats sur le market", ["result"])  # success | insufficient_funds | error
TRADES = Counter("app_trades_total", "Échanges", ["status"])  # created | accepted | refused | cancelled
ACTIVE_SESSIONS = Gauge("app_active_sessions", "Sessions utilisateur valides")
IGDB_IMPORT_DURATION = Histogram("app_igdb_import_duration_seconds", "Durée de l'import IGDB")
IGDB_REQUESTS = Counter("app_igdb_requests_total", "Appels à l'API IGDB", ["endpoint", "status"])
IGDB_LAST_SUCCESS = Gauge("app_igdb_last_success_timestamp_seconds", "Dernier import IGDB réussi")
```

Usage : `LOGIN_ATTEMPTS.labels(result="success").inc()` dans `routes/auth.py`, etc.

| Prio | Metric | Ce qu'on regarde dans Grafana |
|---|---|---|
| P1 | `app_login_attempts_total{result}` | Logins réussis vs échoués/min → détection de brute force |
| P1 | `app_active_sessions` | Nombre d'utilisateurs connectés |
| P2 | `app_cards_dropped_total{rarity,shiny}` | **Distribution réelle des raretés** vs taux théoriques → vérifie que le RNG des boosters est correct |
| P2 | `app_boosters_opened_total` | Activité du jeu (boosters/heure) |
| P2 | `app_purchases_total{result}` | Achats réussis vs échoués sur le market |
| P2 | `app_trades_total{status}` | Échanges proposés / acceptés / refusés |
| P2 | `app_igdb_requests_total{status}` + `app_igdb_import_duration_seconds` | Santé de la dépendance externe IGDB (token, rate-limit 429, erreurs) |
| P3 | Nombre total d'users / cartes en BDD | Via `queries.yaml` custom du postgres_exporter (ex: `SELECT count(*) FROM users`) |
| P3 | Économie : monnaie en circulation, prix moyen au market | Détecter une inflation / un exploit de duplication |

Exemple de panel « RNG des boosters » :
`sum by (rarity) (increase(app_cards_dropped_total[24h])) / ignoring(rarity) group_left sum(increase(app_cards_dropped_total[24h]))`

---

## 4. Alertes

Toutes dans `prometheus/alerts.yml`. Convention : `severity: critical` = action immédiate, `warning` = à regarder dans la journée.

### 4.1 Disponibilité

| Prio | Alerte | Expression | for | Sévérité |
|---|---|---|---|---|
| ✅ | `TargetDown` (existe) | `up == 0` | 1m | critical |
| P1 | `ContainerRestarting` | `time() - container_start_time_seconds{name=~"backend\|nginx\|db"} < 120` | 0m | warning |
| P1 | `ContainerCrashLoop` | `changes(container_start_time_seconds{name=~"backend\|nginx\|db"}[15m]) > 3` | 0m | critical |
| P1 | `PostgresDown` | `pg_up == 0` | 1m | critical |
| P2 | `WebsiteDown` (blackbox) | `probe_success == 0` | 2m | critical |
| P3 | `SSLCertExpiringSoon` | `probe_ssl_earliest_cert_expiry - time() < 14*86400` | 1h | warning |

### 4.2 Performance / erreurs API

| Prio | Alerte | Expression | for | Sévérité |
|---|---|---|---|---|
| P1 | `HighErrorRate` | `sum(rate(http_requests_total{status="5xx"}[5m])) / sum(rate(http_requests_total[5m])) > 0.05` | 5m | critical |
| P1 | `HighLatencyP95` | `histogram_quantile(0.95, sum by (le) (rate(http_request_duration_seconds_bucket{handler!="/metrics"}[5m]))) > 1` | 10m | warning |
| P2 | `NoTraffic` | `sum(rate(http_requests_total{handler!="/metrics"}[15m])) == 0` | 30m | warning |

### 4.3 Ressources

| Prio | Alerte | Expression | for | Sévérité |
|---|---|---|---|---|
| P1 | `HostHighCpu` | `100 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100 > 90` | 10m | warning |
| P1 | `HostHighMemory` | `100 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes * 100 > 90` | 5m | warning |
| P1 | `HostDiskAlmostFull` | `100 - node_filesystem_avail_bytes{mountpoint="/"} / node_filesystem_size_bytes{mountpoint="/"} * 100 > 85` | 5m | warning (critical > 95) |
| P2 | `HostDiskWillFillIn24h` | `predict_linear(node_filesystem_avail_bytes{mountpoint="/"}[6h], 86400) < 0` | 30m | warning |
| P2 | `ContainerHighMemory` | `container_memory_working_set_bytes{name!=""} / container_spec_memory_limit_bytes{name!=""} > 0.9` (nécessite des `mem_limit` dans le compose) | 5m | warning |
| P2 | `PostgresTooManyConnections` | `sum(pg_stat_database_numbackends) / max(pg_settings_max_connections) > 0.8` | 5m | warning |
| P3 | `PostgresDeadlocks` | `increase(pg_stat_database_deadlocks[10m]) > 0` | 0m | warning |

### 4.4 Sécurité / métier

| Prio | Alerte | Expression | for | Sévérité |
|---|---|---|---|---|
| P1 | `LoginBruteForce` | `sum(rate(app_login_attempts_total{result!="success"}[5m])) * 60 > 20` (> 20 échecs/min) | 2m | warning |
| P2 | `IgdbApiErrors` | `sum(rate(app_igdb_requests_total{status!~"2.."}[10m])) > 0` | 10m | warning |
| P2 | `PurchaseFailures` | `sum(rate(app_purchases_total{result="error"}[10m])) > 0` | 5m | warning |
| P3 | `AbnormalLegendaryRate` | taux de légendaires sur 24h > 2× le taux théorique (bug ou exploit) | 1h | warning |
| P3 | `BackupTooOld` | `time() - backup_last_success_timestamp_seconds > 26*3600` | 0m | critical |

### 4.5 Monitoring du monitoring

| Prio | Alerte | Expression | for | Sévérité |
|---|---|---|---|---|
| P2 | `AlertmanagerNotificationsFailing` | `rate(alertmanager_notifications_failed_total[5m]) > 0` (ex: webhook Discord cassé) | 5m | critical |
| P2 | `PrometheusRuleEvaluationFailures` | `increase(prometheus_rule_evaluation_failures_total[5m]) > 0` | 0m | warning |
| P3 | `Watchdog` | `vector(1)` — alerte toujours active, prouve que la chaîne d'alerting marche | — | none |

---

## 5. Améliorations Alertmanager

- [ ] **P1** `send_resolved: true` sur le receiver Discord (recevoir le message quand c'est réparé).
- [ ] **P1** Ajouter `annotations.description` avec la valeur (`{{ $value | humanize }}`) et `{{ $labels.instance }}` dans chaque alerte.
- [ ] **P2** `group_by: ['alertname', 'severity']` + routes séparées : `critical` → `repeat_interval: 30m`, `warning` → `repeat_interval: 4h`.
- [ ] **P2** `inhibit_rules` : si `TargetDown` pour le backend est active, ne pas envoyer `HighErrorRate` / `HighLatencyP95` (évite le spam).
- [ ] **P3** Tester les alertes avec `amtool` ou en coupant volontairement un conteneur (`docker stop backend`).

---

## 6. Dashboards Grafana à créer

- [ ] **P1** *Infra* (existe) → ajouter une ligne **Conteneurs** (cAdvisor) et une ligne **PostgreSQL**.
- [ ] **P1** *Backend / API* : RED method — **R**ate (req/s), **E**rrors (% 5xx, 4xx), **D**uration (p50/p95/p99) par route.
- [ ] **P2** *Jeu / métier* : utilisateurs connectés, logins, boosters ouverts, distribution des raretés, achats, échanges, santé IGDB.
- [ ] **P3** *Alerting* : panel « alertes actives » (`ALERTS{alertstate="firing"}`) et historique.

---

## 7. Sécurité du monitoring (à ne pas oublier)

- [x] `/metrics` du backend n'est **pas** accessible via nginx (vérifié : `/api/metrics` → 404, `/metrics` → page du front). À revérifier si le `proxy_pass` change.
- [ ] Ports Prometheus / Grafana / Alertmanager uniquement sur `127.0.0.1` (déjà le cas ✅).
- [ ] Le `stub_status` nginx sur un port interne non publié.
- [ ] Ne pas mettre d'identifiants dans les labels des metrics (pas d'email / username en label → aussi mauvais pour la cardinalité).

---

## Ordre conseillé

1. Corriger la query p95 de `notes/query.md` + alertes P1 ressources/erreurs (rien à installer).
2. cAdvisor + alertes conteneurs (on aurait détecté le crash-loop du backend).
3. postgres_exporter + alertes BDD.
4. Metrics métier login/sessions + alerte brute force.
5. Dashboard *Backend / API* (RED).
6. Le reste (blackbox, nginx exporter, metrics jeu, backups, inhibitions).
