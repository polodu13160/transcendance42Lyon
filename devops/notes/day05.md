# Days-05

*explication de tous ce que j'ai fait le 17/11*

## Dockerfile du Backend

On change le WORKDIR de la racine pour evité qu'il soit mélangé avec tous les autres dossier comme /bin /etc ainsi de suite.

On change l'utilisateur pour lancer le container en mode non root.
On fait ca pour eviter que si l'application est compromise. Par exemple si une des dépendance a une faille un attaquant n'est pas les permissions si il sort du container.

```Dockerfile
RUN useradd --create-home appuser && chown -R appuser /code
USER appuser
```

## Dockerfile du frontend

J'ai crée une image docker qui a pour but de build le code du front et une image nginx-unprivileged qui va permettre de lancer nginx en non root sans devoir creer et configurer un utilisateur non root, car l'image le fait deja.

J'ai ensuite rajouté le services dans le compose. Pour l'instant il n'est pas lié au WAF mais ca sera a modifier plus tard.

## Docker-compose global

Creation des services du backend et de la db en premier.
Healthcheck de la db avec CMD-SHELL.

CMD exécute directement le programme, sans shell. Personne ne remplace les variables, donc pg_isready recevrait littéralement la chaîne ${POSTGRES_USER} comme nom d'utilisateur.

Adminer et Nginx sont sur le même port => à corriger

Healthcheck du backend avec CMD.

## Makefile global

J'ai fait un makefile classique et simple avec un make, make build, make down etc..