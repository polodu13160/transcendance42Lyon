# Transcendance 42 Lyon - BACKEND

**Version:** 0.01.0 (Dev)

## Prerequisites

To manage dependencies and environments, this project uses `uv`. 
You must install it first:

```bash
pip install uv
```

>[!WARNING]
>if not pip for install pip, check to internet (67 mentality)

## Getting Started

To set up the project and start the development server, run the following commands at the root of the project:

```bash
uv sync
```

after create .env with the root of directory backend :


````
/src/.env
DATABASE_URL=postgresql://userRoot:PasswordRoot@ip:Port/NameBD
CLIENT_ID=dummy
CLIENT_SECRET=dummy
GRANT_TYPE=client_credentials
````

>[!WARNING]
>Avoir lancer la bdd c pas compliqué c un docker-compose
    Actuellement le mdp c toi qui choisit, et le user root c root (simple comme le mot simple)

And run :

```bash
uv run alembic upgrade head
python -m app.script_wrapper.wrapper
uv run dev

```

```bash
cd backend
pyenv install 3.12
python -m venv .venv
source /home/login/../transcendance42Lyon/backend/.venv/bin/activate
alembic upgrade head
```

## API Documentation - see the good URL fonctionnal

Once the backend is running (via the `uv run dev` command), the interactive API documentation (Swagger UI) is automatically generated and available at:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


## Research for me

* [Alembic Migration Guide (FR)](https://blog.stephane-robert.info/docs/developper/programmation/python/sqlachemy-2/)

* uv run sqlacodegen "postgresql://root:dd@localhost:5432/principal_db" > models.py

* https://www.zhihu.com/en/answer/12830991 - comment calculer la valeur de la carte  
