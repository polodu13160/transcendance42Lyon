# httpbin
httpbin est un backend simpliste pour faire des tests, on lui envoie des requêtes et il retourne ce qu'il a reçu

## lib.sh
Sert de reference pour `legit.sh` et `attacks.sh`

## ligit.sh
Script contenant des requêtes legit

## attacks.sh
Script contenant des requêtes malveillantes

# Tests de requêtes malveillantes

### Attaque XSS
```bash
curl -i -G http://127.0.0.1:8080/get --data-urlencode "q=<script>alert(1)</script>"
```

### Injection SQL
```bash
curl -i -G http://127.0.0.1:8080/get --data-urlencode "id=1' OR '1'='1"
```
Pour lire les logs plus facilement :
```bash
docker compose logs --no-log-prefix --since 30s meow | grep '"transaction"' | tail -1 | jq .
```

Les éléments importants sont :
```JSON
// JSON
"message": "SQL Injection Attack Detected via libinjection", // ou "XSS Attack Detected via libinjection",
"ruleId": "942100", // 941xxx pour attaque XSS ou 942xxx pour injection SQL
"data": "Matched Data: 1&sos found within ARGS:id: 1 OR '1'='1", // l'élément qui a fait réagire la règle
"message": "Inbound Anomaly Score Exceeded (Total Score: 8)", // score d'anomalie
```