##Architecture du projet
``` 
mon_projet/
├── app/
│   ├── main.py                 # Point d'entrée de l'application
│   ├── core/                   # Configuration et logique transversale
│   │   ├── config.py           # Variables d'environnement (Pydantic BaseSettings)
│   │   ├── security.py         # Hashing, génération de tokens JWT
│   │   └── exceptions.py       # Gestionnaires d'erreurs personnalisés
│   ├── api/                    # Contrôleurs et routage
│   │   ├── dependencies.py     # Injections de dépendances (ex: get_db, get_current_user)
│   │   ├── router.py           # Routeur principal qui regroupe toutes les routes
│   │   └── routes/             # Endpoints organisés par domaine
│   │       ├── users.py
│   │       └── items.py
│   ├── models/                 # Modèles SQLAlchemy (Structure de la base de données)
│   │   ├── base.py             # Base déclarative SQLAlchemy
│   │   ├── user.py
│   │   └── item.py
│   ├── schemas/                # Modèles Pydantic (Validation des entrées/sorties)
│   │   ├── user.py             # UserCreate, UserResponse, etc.
│   │   └── item.py
│   ├── crud/                   # Logique d'accès aux données (Create, Read, Update, Delete)
│   │   ├── crud_user.py
│   │   └── crud_item.py
│   ├── db/                     # Configuration de la base de données
│   │   ├── session.py          # Création de l'engine et SessionLocal
│   │   └── migrations/         # Dossier généré par Alembic
│   └── middlewares/            # Intercepteurs de requêtes HTTP
│       ├── cors.py             # Configuration CORS (accepter certains domaines)
│       └── logging.py          # Logs des requêtes et temps d'exécution
├── tests/                      # Tests unitaires et d'intégration (Pytest)
│   ├── conftest.py             # Fixtures Pytest
│   └── api/
├── .env                        # Fichier de variables d'environnement
├── alembic.ini                 # Configuration des migrations de base de données
└── pyproject.toml            # Dépendances du projet

``` 

## Reflexion de travail 


1. Tout d'abord je dois importer ma bdd pour avoir une base solide avec alembic.
afin que mes models soient bien generés, savoir faire aussi l'inverse car par la suite on fera la migration de fastapi a postgre

2. faire des seeders et des factory pour remplir la bdd ( a skip avec la lib Faker et non je ne parle pas de la personne looooooooool)

3. faire le crud sur chacune de mes tables (create read update delete)

3. faire le middleware 
    il a le droit ou pas de faire cette requete https (connecté ou pas ?) alors rectification sur fastapi ca sera avec des depends 
    ```
    
    Dossier middlewares/ : Pour les actions globales et aveugles sur le trafic HTTP. (ex: CORS, mesurer le temps d'exécution d'une requête, bloquer une IP qui spamme, logs globaux).
    Fichier api/dependencies.py : Pour la logique métier liée à une requête spécifique. (ex: "Cet utilisateur est-il connecté ?", "Est-il administrateur ?", "Ouvrir une session avec la base de données").

4. faire les routes 

