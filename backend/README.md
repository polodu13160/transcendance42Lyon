
## Prerequisites

  

To manage dependencies and environments, this project uses `uv`.

You must install it first:

```bash

pip install uv

```

>[!WARNING]

>if not pip for install pip, check to internet (67 mentality)


# Getting Started - Init BDD for backend

  

## To set up the PostGresSql :


> [!NOTE] path 
> **transcendance42Lyon/bdd/server**

- [ ] <u>after that run the bdd docker in </u>
```bash

cd ./transcendance42Lyon/bdd/server
#create a file in new folder :
mkdir srcs/secrets/
echo -n 'password' > srcs/secrets/secretsPostGres_Password 
#in this file create add pasword of the user ROOT of BDD(no return line)
#for modif the user PostGreSql check the transcendance42Lyon/bdd/server/makefile
mkdir srcs/data-test
docker compose up -d
`````

- [ ] <u>check in the navigator if you re acces to adminer in this address</u> :

```bash
https://localhost:8080
`````

- [ ] <u>and filled in this way</u> : 

| var      | value                                                                                          |
| -------- | ---------------------------------------------------------------------------------------------- |
| Systeme  | PostgreSQL                                                                                     |
| Serveur  | localhost **==🔴except if the backend in the docker, use the name docker compose of the db==** |
| user     | check the user in the db dockercompose.yml                                                     |
| password | transcendance42Lyon/bdd/server/secretsPostGres_Password **(password is in the file)**          |
| BDD      | do not fill in the slot                                                                        |



## Getting Started - Init Backend

> [!NOTE] path 
> **transcendance42Lyon/backend**


To set up the backend :

```bash
cd ./transcendance42Lyon/backend/
uv sync
# userRoot is root, passwordRoot is the password, ip is localhost and port is 5432 and nameDB is the name of your new database 
cat .env.exemple > .env
uv sync
#run the dev server 
```


Set up the file .env : 
```.env
DATABASE_URL=postgresql://user:password@localhost:5432/principal_db

CLIENT_ID=jkhkjhkjhkjhkjhjkh

CLIENT_SECRET=hkhkjhkjh

GRANT_TYPE=client_credentials

ENVIRONMENT=DEV
```


| Name var      | description                        | detail                                                                                                                                                                                                               |
| ------------- | ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DATABASE_URL  | the url for connect backend to bdd | `user = userPostGres`<br>`password = userPassword in the secrets folder`<br>`localhost` = the ip use for db<br>`5432 = it is the port of the db`<br>`principal_db = it is the chosen name for the database` <br><br> |
| CLIENT_ID     | the id connection use for IGDB api | check account creation : <br>[click here](https://api-docs.igdb.com/#getting-started)                                                                                                                                |
| CLIENT_SECRET | the secret for connection IGDB api | after account creation:<br>[click here](https://dev.twitch.tv/console/apps)                                                                                                                                          |
| ENVIRONMENT   | it is the choice environment.      | `ENVIRONMENT=PROD if don't want factories users and other tests`<br>`ENVIRONMENT=DEV if you want factories users and other tests`                                                                                    |
| GRANT_TYPE    | use the value `client_credentials` |                                                                                                                                                                                                                      |


> [!FINISH] Run the fastApi Backend
> path:
> **transcendance42Lyon/backend**
> command:
```
uv run fastapi dev
```
> 
