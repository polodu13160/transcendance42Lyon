Dans ce days on test un backend "factice" pour parametrer Prometheus et Grafana.

Question:

Quel nom a pris games_played sur /metrics ? Quelle relation vois-tu entre _count et le bucket le="+Inf" ?

game_played à pris le nom: Nombre de parties jouées.
On voit bien que la valeur entre count et le="+Inf" est la même.

Comprendre le code:

1 - Que fait le middleware ? Pourquoi les métriques HTTP sont-elles mesurées là plutôt que dans chaque route ?

Le middleware va faire un calcul de la duré des request.

2 - Le label route reçoit /games/{game_id} et pas /games/42. Pourquoi ? (Reprends la cardinalité.)

Car c'est pas toujours l'id 42 qu'on va vouloir voir mais tous les game id possible.

3 - Que vaut le label route pour une URL inexistante (essaie curl localhost:8000/nimportequoi), et pourquoi ?

Le label route recoit : "unmatched". Car il n'y  a pas eu de rout crée avec ce nom.

4 - Dans create_game, mode est limité à "solo" ou "multi". Teste ?mode=truc : que se passe-t-il ? Pourquoi est-ce important pour un label ?



5 - Pourquoi des buckets personnalisés plutôt que ceux par défaut ? Relie-le à ton p95 de 95 ms constant du Jour 3.

Pour l'exercice 