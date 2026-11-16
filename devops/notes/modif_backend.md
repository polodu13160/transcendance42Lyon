# Modification du backend pour ajout prometheus.

J'ai rajouté dans main.py les lignes suivantes:

```py
from prometheus_fastapi_instrumentator import Instrumentator

Instrumentator().instrument(app).expose(app)
```

J'ai aussi rajouté une ligne dans le backend pour installer les dépendences de instrumentator: 
`uv add prometheus-fastapi-instrumentator`

J'ai aussi commenté les lignes du main.py qui n'étaient plus necessaire car on a plus besoin de bet() entre autres.

Vérifié que les metrics ne soit pas exposé via le reverse proxy.