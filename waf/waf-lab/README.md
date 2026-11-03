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
"file": "/etc/modsecurity.d/owasp-crs/rules/REQUEST-942-APPLICATION-ATTACK-SQLI.conf", // le fichier de la règle
```

```bash
docker compose exec meow sed -n '1,40p' /etc/modsecurity.d/owasp-crs/rules/REQUEST-942-APPLICATION-ATTACK-SQLI.conf # pour lire le début de la règle

docker compose exec -T meow cat /etc/modsecurity.d/owasp-crs/rules/REQUEST-941-APPLICATION-ATTACK-XSS.conf | less # pour lire la règle en entier
```

# Exercices pour comprendre le fonctionnement

### Exercice 0 : l’infrastructure
Objectif : comprendre l’architecture.

- Compose avec deux services : waf (image owasp/modsecurity-crs:nginx, BACKEND pointant vers le backend) et backend.
- Seul le WAF a une section ports:.
- Vérifie : curl localhost:8080 répond, et le backend n’est pas joignable directement depuis ta machine.
- Écris lib.sh avec une fonction qui lance un curl, compare le code HTTP reçu au code attendu et affiche PASS/FAIL. Le script doit retourner un code de sortie non nul au moindre échec.

### Exercice 1 : le trafic légitime
Objectif : avoir une référence pour détecter les faux positifs.

- Dans legit.sh, écris 8 à 10 requêtes normales : GET simple, GET avec paramètres, POST de formulaire, POST JSON, header Authorization, etc.
- Tout doit renvoyer 200. Ce script est ton filet de sécurité : tu le relances après chaque modification du WAF.

### Exercice 2 : mode détection
Objectif : apprendre à lire les logs.

- Passe le moteur en DetectionOnly, puis envoie un XSS et une injection SQL.
- Les requêtes passent (200), mais le WAF les journalise. Dans les logs, retrouve le numéro de règle, le message et le score d’anomalie.
- Question : quelle règle a déclenché, et dans quel fichier de CRS se trouve-t-elle ?

### Exercice 3 : mode blocage et catalogue d’attaques
Objectif : écrire attacks.sh.

- Passe en On : les attaques doivent maintenant renvoyer 403.
- Teste au moins une attaque par famille :

| Famille | Idée de payload | Fichier CRS |
| --- | --- | --- |
| SQLi | ?id=1' OR '1'='1 | 942 |
| XSS | ?q=<script>alert(1)</script> | 941 |
| Path traversal | ?file=../../etc/passwd | 930 |
| Injection de commande | ?cmd=;cat /etc/passwd | 932 |
| Scanner | User-Agent: sqlmap | 913 |
| Protocole	| header malformé, méthode inhabituelle | 920 |

- Pour chaque attaque, note quelle règle a bloqué (via les logs).


### Exercice 4 : le score d’anomalie
Objectif : comprendre que CRS ne bloque pas sur une seule règle.

- Chaque règle déclenchée ajoute des points. Le blocage a lieu quand le total dépasse un seuil (la règle d’évaluation est la 949110).
- Trouve une requête qui déclenche une règle sans être bloquée, puis modifie-la pour cumuler assez de points.
- Change le seuil via la variable d’environnement de l’image (voir le README) et observe l’effet.

### Exercice 5 : les niveaux de paranoïa
Objectif : voir le compromis sécurité / faux positifs.

- Écris un script qui envoie le même lot de requêtes (attaques + légitimes) aux niveaux 1, 2, 3 et 4, et affiche une matrice.
- Question : à partir de quel niveau tes requêtes légitimes commencent-elles à être bloquées ?

### Exercice 6 : l’évasion par encodage
Objectif : comprendre que le WAF normalise les entrées.

- Prends ton XSS et ton SQLi et déguise-les : URL-encoding, double encoding, casse mélangée (SeLeCt), commentaires SQL (UN/**/ION).
- Sont-ils toujours bloqués ? Lesquels passent éventuellement, et à quel niveau de paranoïa sont-ils attrapés ?

### Exercice 7 : un faux positif et son exclusion
Objectif : apprendre à régler sans affaiblir la protection.

- Provoque un faux positif avec une requête légitime (un champ de texte contenant par exemple select ... from, ou du HTML dans un JSON).
- Trouve la règle responsable dans les logs, puis écris une exclusion dans REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf.
- Compare deux approches : supprimer la règle entièrement, ou exclure seulement l’argument concerné. La seconde est la bonne pratique.
- Validation : legit.sh passe et attacks.sh bloque toujours tout.

### Exercice 8 : une règle écrite à la main
Objectif : apprendre la syntaxe SecLang.

- Écris une règle qui bloque une condition de ton choix, par exemple un header X-Evil: 1 ou l’accès à /admin. Utilise un identifiant dans la plage réservée à l’usage local (1 à 99999).
- Variante : une règle qui journalise sans bloquer.
- Ajoute des tests dans attacks.sh pour la règle.

### Exercice 9 : corps de requête et réponses (avancé)
- Envoie un gros body ou un upload : quelle limite te bloque, et comment l’ajuster ?
- Fais renvoyer par le backend un message d’erreur typique (par exemple une erreur SQL) et regarde si les règles de réponse (famille 95x) réagissent.

### Exercice 10 : industrialiser
Objectif : rendre la suite réutilisable sur ton vrai projet.

- Paramètre l’URL de base. Ajoute un script run-all.sh qui lance legit.sh puis attacks.sh et retourne un code d’erreur global.
- Bonus : lance un scanner automatique (nikto, OWASP ZAP, sqlmap) depuis un autre conteneur contre ton WAF et regarde ce qui est bloqué.
- Pour aller plus loin, regarde go-ftw, l’outil de test officiel de CRS.

### Bonus : prouver que la suite est indépendante du moteur
Refais l’exercice 0 avec la solution B (ton propre Dockerfile Debian), puis avec coraza-crs:nginx. Si run-all.sh donne les mêmes résultats, tes tests mesurent bien le comportement du WAF et pas les détails d’un montage particulier.

Quand tu auras écrit tes premiers scripts (lib.sh et legit.sh), envoie-les-moi et je les relirai avec toi avant que tu passes aux attaques.
