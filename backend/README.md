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
uv venv
uv sync
```

after create .env with the root of directory backend :


````
/src/.env
DATABASE_URL=postgresql://userRoot:PasswordRoot@ip:Port/NameBD 
````

And run :

```bash
uv run dev
```


## API Documentation

Once the backend is running (via the `uv run dev` command), the interactive API documentation (Swagger UI) is automatically generated and available at:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

*Note: Currently, only one API endpoint is fully functional and documented on this page. and is used just for integrations, not endpoint final*

## Research for me

* [Alembic Migration Guide (FR)](https://blog.stephane-robert.info/docs/developper/programmation/python/sqlachemy-2/)

* uv run sqlacodegen "postgresql://root:dd@localhost:5432/principal_db" > models.py
