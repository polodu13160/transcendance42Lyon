# Toutes les métrics du projets expliqué:

### Metrics systèmes:

On récupère les metrics système avec node exporter.
Cela va nous donner des indications sur la machine host qui lance le programme:

**Target UP**:

Nous indique le nombre de targets qui sont UP(par exemple prometheus, le backend, la bdd etc..)

**% CPU usage**:

Nous donne le % de CPU qu'on est entrain d'utilisé sur notre machine hote.

**Memory usage**:

Nous donne le % de memoire(RAM) qu'on est entrain d'utilisé sur notre machine hote.

**Disk usage**:

Nous donne le % de mémoire sur notre disque qu'on est entrain d'utiliser.

**Network flow state**:

Cette métrics affiche le débit réseau entrant par interface de la machine hote. Ca permet de vérifier le trafic arrive bien sur la machine ou si il y a des pics qui pourrait induire un spam du front sur l'API en boucle par exemple.

### Metrics Prometheus

**Latence**:

Le p50, p95, p99 de la latence des requettes de prometheus.

**Request**:

Le nombres de requests par secondes sur Prometheus.

### Metrics Backend

**Request/s by route**:

Nombre de requests par second par route sur le backend FastAPI.

**Latence**

Donne la latence au 95 percentile de chaque endpoint du backend sur les 5 derniere minutes. En gros pour chaques route de mon API, 95% des request ont repondue en X secondes.

**Error rate**

Nous donne un pourcentage du nombre d'erreur 5xx.

### Metrics de postgres

**Database UP**:

Indique simplement si la database est UP ou pas.

**Used Connection**:

Indique le taux de remplissage des connexions Postgres.
Donne en pourcentage par rapport au nombre max de connection possible combien de slot de connexion sont occupés.

**Cache hit ratio**:

Cette metrics permet de mesurer le pourcentage de lectures servies depuis la RAM.
En effet lorsque Postgre stocke les données sur disque il garde les blocs les plus utilisé en RAM.
'hit' représente la lecture sur RAM.
'read' représente la lecture sur le disque.
Si le pourcentage baisse ca veut dire que la base ne tient plus en RAM ou une requête lit des tables entières, et il faut augmenter la mémoire ou ajouter un index.

**Transaction**:

Nous donne le nombre de connexion en `idle in transaction`.
Une connexion peut etre dans plusieurs états:
`active` : elle exécute une requête en ce moment ;
`idle` : elle ne fait rien et attend. C'est normal pour une connexion de pool.
`idle in transaction` : elle a ouvert une transaction (BEGIN), elle ne fait plus rien, mais la transaction n'a été ni validée (COMMIT) ni annulée (ROLLBACK).
Si elle reste en idle in transaction cella veut dire qu'elle ne peut ni etre nettoyé, bloquer potetiellement les autres requetes et occupe une connexion.

