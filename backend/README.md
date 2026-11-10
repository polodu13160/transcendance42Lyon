
## Prerequisites

  

To manage dependencies and environments, this project uses `uv`.

You must install it first:

```bash

pip install uv

```

>[!WARNING]

>if not pip for install pip, check to internet (67 mentality)


## Getting Started - Init BDD

  

To set up the PostGresSql :

  

after that run the bdd docker in 
```bash

cd ./transcendance42Lyon/bdd/server
#create a file in new folder :
mkdir -r srcs/secrets/
echo -n 'password' > srcs/secrets/secretsPostGres_Password 
#in this file create add pasword of the user ROOT of BDD(no return line)
mkdir srcs/data-test
docker compose up -d
`````

check in the navigator if you re acces to adminer in this address :

```bash
https://localhost:8080
`````

and use the password created in the file `srcs/secrets/secretsPostGres_Password `



## Getting Started - Init Backend


To set up the backend :

in the first time :

> [!WARNING] Create in the BDD the name of the database
> the simplest method is access with adminer and create the database with name of your choice

```bash
cd ./transcendance42Lyon/backend/
uv sync
# userRoot is root, passwordRoot is the password, ip is localhost and port is 5432 and nameDB is the name of your new database 
echo 'DATABASE_URL=postgresql://userRoot:PasswordRoot@ip:Port/NameBD' > .env
uv run alembic upgrade head
#if not fonctionnal, you´re idiot
make init_db 
#init db to get cards
make init_user
#init tom and bob user 
make run_dev
#run the dev server 
```







[^1]: 
