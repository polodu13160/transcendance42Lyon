# User Stories et Endpoints
---

> [!WARNING]
> -->**TOUTE LES DATES SONT EN UTC(00+)
>-->Tout ce qui est Authorization a mettre dans le header ne sont pas a prendre en compte pour le moment (mettre dans le body juste le user_id si besoin)
>-->TOUTES LES PAGINATIONS SONT PAR TRANCHE DE 10**
>-->**LE PRIX LE PLUS HAUT EST DE 10000 tokens (c ok comme ca on peut pas etre en overfloooooooooooooooooooooooooooooooooooooooooow)**


## 1. Modèles Génériques (Schemas)

Ces structures de données sont réutilisées à travers l'ensemble des endpoints. Lorsqu'un modèle générique apparaît dans une réponse JSON (en Majuscule), se référait a ces schemas de données


### `CARD
```json
{
  "id": "uuid | int",
  "name": string,
  "colors": int:[possibility : 1,2,3,4] ,
  "description": text
  "name_franchise": string,
  "image_url": [string(noshiny), string(shiny)],
  "value_exchange_min": float | int,
  "attq": int,
  "def" : int,
  "url_IGBD": string,
  "game_type": int [1: dlc, Other: main_game]
  "parent_id": int (juste pour les dlcs)
  "genre": {"string,string..."}
  "company_game": {"string,string..."}
}
```

### `USER
```json
{
  id_user: int,
  last_name: char(100),
  first_name: char(100),
  nick_name: char(100),
  date_created: timetampz,
  id_wallet: int,
  amount_crypto: float,
  date_free_pack: timetampz
}
```

### CARD_USER (joint toujours avec CARD
```json
{
  "is_shiny": bool,
  "is_favorite": bool,
  "is_auction": bool,
  "time_acquisition":timestamptz,
  "id_user":integer,
  "time_limit_auction": timestamptz | NULL, #if auction is true else NULL
  "time_created_auction":timestamptz | NULL, #if auction is true else NULL
  "is_finish_auction": false,
 
}
```

---

### Template Schema
### XXXX
```json
{
  "XXX": bool,
}
```

---

## 2. User Stories & Endpoints

---

### US-01 : Authentification de session
> **En tant qu'** utilisateur  
> **Je veux** pouvoir me connecter avec mes identifiants  
> **Afin d'** ouvrir une session personnelle et accéder aux échanges, achats et ventes et a ma collection.

* **Endpoint :** `POST /api/v1/auth/login`
* **Headers :** `Content-Type: application/json`

#### Request Body
```json
{
  "pseudo": "Toto",
  "password": "Trotrorigolo"
}
```

#### Responses
* **`200 OK`** : Connexion réussie, session active
  ```json
  {
    "token": "jwt_token_string",
    "user": {USER}
  }
  ```
* **`401 Unauthorized`** : Identifiant ou mot de passe incorrect
  ```json
  {Error Unauthorized}
  ```

---

### US-02 : Consultation de l'historique d'achats
> **En tant qu'** utilisateur connecté  
> **Je veux** consulter mon historique d'achats avec pagination (par tranches de 10)  
> **Afin de** suivre mes dépenses en détail.

* **Endpoint :** `GET /api/v1/purchases/history` (ou `/history_purchases`)
* **Headers :** `Authorization: Bearer <token>`
* **Query Parameters :**
  * `page` *(int, default: 0)* : Index de la page

#### Responses
* **`200 OK`** : Liste des transactions paginées
  ```json
  {
    "page": 0,
    "total_count": 42,
    "items": [
      {
        "id": "uuid | int",
        "value_crypto": float,
        "purchase_sum": float,
        "quantity_crypto": int,
        "date": "2026-11-02T14:30:00Z"
      }
    ]
  }
  ```
* **`401 Unauthorized`** : Session invalide ou expirée
  ```json
 {Error Unauthorized}
  ```

---

### US-03 : Vente directe de cartes (prix système défini)
> **En tant qu'** utilisateur  
> **Je veux** vendre une carte au prix défini par défaut  
> **Afin de** libérer des fonds instantanément pour en acheter d'autres.

* **Endpoint :** `POST /api/v1/cards/sell` 
* **Headers :** `Authorization: Bearer <token>`, `Content-Type: application/json`

#### Request Body
```json
{
  "card_id": "int",
  "id_user": "int"
}
```

#### Responses
* **`200 OK`** : Vente confirmée
  ```json
  {
    "status": "sold",
    "card_id": "uuid | int",
    "amount_credited": 12.50,
    "amount_crypto": 145.20
  }
  ```
* **`400 Bad Request`** : carte non possédée
  ```json
  {Error Unauthorized}
  ```
* **`401 Unauthorized`** : Non authentifié ou non autorisé
  ```json
  {Error Unauthorized}
  ```

---

### US-04 : Mise en vente sur le Marketplace
> **En tant qu'** utilisateur  
> **Je veux** mettre une carte en vente sur la place de marché à un prix libre  
> **Afin de** la vendre plus cher que son prix fixe de reprise.

* **Endpoint :** `POST /api/v1/market
* **Headers :** `Authorization: Bearer <token>`, `Content-Type: application/json`

#### Request Body
```json
{
  "card_id": "int",
  "min_price": 25.00
}
```

#### Responses
* **`201 Created`** : Carte mise sur le marché avec succès
  ```json
  {
    "listing_id": "int",
    "status": "listed",
    "card": CARD,
    "seller_id": "uuid | int",
    "min_price": 25.00,
    "created_at": "2026-11-02T15:00:00Z"
  }
  ```
* **`400 Bad Request`** : carte non possédée
  ```json
  {Error Unauthorized}
  ```
* **`401 Unauthorized`** : Non authentifié ou non autorisé
  ```json
  {Error Unauthorized}
  ```
* **`422 Unprocessable Entity`** : Prix inférieur au prix plancher ou durée invalide
  ```json
  {The price is too low} or  {The price is too high} 
  ```

---

### US-05 : Recherche et filtres Marketplace
> **En tant qu'** utilisateur  
> **Je veux** rechercher des cartes en vente via des filtres combinés (nom, couleur, franchise, tri chronologique, shiny, pagination par 10)  
> **Afin de** trouver et acheter des cartes spécifiques rapidement.

* **Endpoint :** `GET /api/v1/market
* **Headers :** Optionnel
* **Query Parameters :**
  * `name` *(string, optionnel)* : Filtre par nom
  * `colors` *(string, optionnel)* : Liste séparée par virgules (ex: `Red,Blue`)
  * `franchises` *(string, optionnel)* : Ex: `Pokemon`
  * `is_shiny` *(boolean, optionnel)* : `true` ou `false`
  * `time_limit_sort` *(enum: asc | desc, default: desc)* : Tri sur la date de fin
  * `page` *(int, default: 0)* : Numéro de page

#### Responses
* **`200 OK`** : Lot de 10 résultats filtrés
  ```json
  {
    "page": 0,
    "total_results": 85,
    "items": [
      {
        "listing_id": "uuid | int",
        "card": CARD,
        "card_user": CARD_USER
        "price": 34.00,
        "time_remaining_seconds": 7200,
        "listed_at": "2026-11-02T12:00:00Z"
      }
    ]
  }
  ```
* **`400 Bad Request`** : Paramètre de filtre mal formé
  ```json
  {Wrongs Filters}
  ```

### US-06 : Consultation et tri de la collection personnelle
> **En tant qu'** utilisateur connecté  
> **Je veux** accéder à ma collection personnelle de cartes et pouvoir la trier  
> **Afin de** visualiser l'ensemble des cartes que je possède mais aussi si j'ai toute les cartes d'une franchise (un pourcentage de possession (faire sur le front))

* **Endpoint :** `GET /api/v1/collection`
* **Headers :** `Authorization: Bearer <token>`
* **Query Parameters :**
  * `sort_by` *(enum: name | date_acquired | base_value | rarity, default: date_acquired)*
  * `order` *(enum: asc | desc, default: desc)*
  * `page` *(int, default: 0)*
  pas obligatoire:
  * `name_franchise`  
  * `name_collection`  
  * `is_shiny` 
  * `colors` 
  * `genre`
  * `is_dlc` (si true que les dlcs si false pas de dlc)

#### Responses
* **`200 OK`** : Cartes possédées par l'utilisateur
  ```json
  {
    "total_cards": 128,
    "page": 0,
    "items": [
      {
        {"card" : CARD,
         "card_user": CARD_USER},
         "nb_posseded_franchise": int
         "nb_total_franchise" : int
         ...
      }
    ]
  }
  ```
* **`401 Unauthorized`** :
  ```json
    {Error Unauthorized}
  ```

---

### US-07 : Gestion des favoris
> **En tant qu'** utilisateur connecté  
> **Je veux** ajouter ou retirer une carte de mes favoris  
> **Afin de** retrouver rapidement mes cartes préférées dans ma collection.

* **Endpoint :** `PATCH /api/v1/collection/cards/{card_id}/favorite`
* **Headers :** `Authorization: Bearer <token>`, `Content-Type: application/json`

#### Request Body
```json
{
  "is_favorite": true
}
```

#### Responses
* **`200 OK`** : Statut du favori mis à jour
  ```json
  {
    "card_id": "int",
    "is_favorite": true
  }
  ```
* **`401 Unauthorized`** :
  ```json
    {Error Unauthorized}
  ```


---

### US-08 : Gestion des collections/dossiers personnalisés
> **En tant qu'** utilisateur connecté  
> **Je veux** créer des classeurs personnalisés nommés et y assigner des cartes  
> **Afin d'** organiser mes cartes selon mes propres critères et préférences.

* **Endpoints :**
  * Créer un classeur : `POST /api/v1/collection/{name_collection}
  * Ajouter une carte : `POST /api/v1/collection/{name_collection}
* **Headers :** `Authorization: Bearer <token>`, `Content-Type: application/json`

SI LA COLLECTION N'EXISTE PAS, CA LA CRéé AUTOMATIQUEMENT
#### Request Body (Ajout de carte dans le dossier)
```json
{
  "card_id": {"int","int"}
}
```

#### Responses
* **`201 Created`** : Dossier créé et/ou carte ajoutée
  ```json
 {Folder [Name] Created}
 and or 
 {[Name Card] add in Folder [Name]}
  ```
* **`400 Bad Request`** : Nom de dossier invalide ou carte déjà présente
  ```json
  {ERROR} (je savais pas quoi dire)
  ```
* **`401 Unauthorized`** : pas connecté
  ```json
    {Error Unauthorized}
  ```
---



---

### US-10 : Achat de paquets de cartes aléatoires
> **En tant qu'** utilisateur connecté  
> **Je veux** dépenser des crédits/crypto pour acheter un pack de cartes aléatoires  
> **Afin de** débloquer de nouvelles cartes pour ma collection ou le marché.


> [!NOTE]
> UN PACK DE CARTES CONTIENT 10 CARTES AU TOTAL 

* **Endpoint :** `POST /api/v1/packs/buy`
* **Headers :** `Authorization: Bearer <token>`, `Content-Type: application/json`

#### Responses
* **`200 OK`** : Pack ouvert et tirage des cartes
  ```json
  {
    "remaining_wallet_balance": 120.0,
    "cards": {
	    card: CARD,
	    card_user: CARD_USER
    }   
  }
  ```
* **`402 Payment Required`** : Solde insuffisant
  ```json
  <span style="color: #2ecc71; font-weight: bold;">ErrorResponse</span>
  ```
* **`401 Unauthorized`** : pas connecté
  ```json
    {Error Unauthorized}
  ```
---

### US-11 : Récupération du paquet quotidien gratuit
>**En tant qu'** utilisateur connecté  
> **Je veux** réclamer un paquet de cartes gratuit une fois par jour (toutes les 24h)  
> **Afin de** récupérer des cartes régulièrement sans avoir à payer.

* **Endpoint :** `POST /api/v1/packs/free
* **Headers :** `Authorization: Bearer <token>`
#### Responses
* **`200 OK`** : Tirage du pack quotidien
  ```json
  {
    "next_claim_available_at": "2026-11-03T16:00:00Z",
    "cards": 
	    {
		    "cards": CARD,
		    "card_user": CARD_USER
	    }
  }
  ```
* **`429 Too Many Requests`** : Pack quotidien déjà réclamé
  ```json
  {
    "error": "COOLDOWN_ACTIVE",
    "message": "Pack déjà récupéré aujourd'hui",
    "available_in_seconds": 43200
  }
  ```
 * **`401 Unauthorized`** : pas connecté
  ```json
    {Error Unauthorized}
  ```
  
---

### US-12 : Rechargement du portefeuille (Achat de crypto du site)
> **En tant qu'** utilisateur connecté  
> **Je veux** acheter de la monnaie virtuelle/crypto dédiée à la plateforme  
> **Afin de** pouvoir acheter des cartes unitaires sur le marché ou des paquets.

* **Endpoint :** `POST /api/v1/wallet`
* **Headers :** `Authorization: Bearer <token>`, `Content-Type: application/json`

#### Request Body
```json
{
  "fiat_amount": 20.00,
  "currency": "EUR",
  "payment_method_token": "tok_visa_1234"
}
```

#### Responses
* **`200 OK`** : Rechargement validé
  ```json
  {
    "transaction_id": "uuid | int",
    "crypto_amount_credited": 200.0,
    "amount_crypto": 350.0,
    "status": "completed"
  }
  ```
* **`400 Bad Request`** : Échec du paiement
  ```json
 {Payment Failed}
  ```

---

### US-13 : Fiche détaillée d'une carte (Modal)
> **En tant qu'** utilisateur  
> **Je veux** ouvrir une vue détaillée pour une carte spécifique avec la full description de toutes les infos de la cartes et les liens   
> **Afin d'** en apprendre plus sur le lore du jeu et découvrir du contenu.

* **Endpoint :** `GET /api/v1/cards/{card_id}/details`
* **Headers :** Optionnel

#### Responses
* **`200 OK`** : Fiche complète de la carte 
  ```json
  {
    "card" : CARD,
    "card_user": CARD_USER 
  }
  ```
* **`404 Not Found`** : Carte inexistante
  ```json
  <span style="color: #2ecc71; font-weight: bold;">ErrorResponse</span>
  ```

---

### US-14 : Navigation en mode Prospect (Visiteur non authentifié)
> **En tant que** prospect (visiteur anonyme)  
> **Je veux** naviguer librement sur l'interface du jeu et voir le catalogue  
> **Afin de** découvrir l'offre, tout en étant invité à me connecter si je tente d'acheter, vendre ou échanger.

* **Endpoint :** `GET /api/v1/public/preview-catalog`
* **Règle de gestion :** Tous les endpoints d'action (`POST /api/v1/packs/*/buy`, `POST /api/v1/cards/sell`, `POST /api/v1/market/*`) renvoient un code `401 Unauthorized` si aucun token de session n'est fourni, déclenchant l'ouverture de la modale de connexion côté client.

#### Responses
* **`200 OK`** : Aperçu public des cartes phares (random de 10 cartes)
  ```json
  {
    "cards": {
	    card: CARD,
	        ...
	    }

  }
  ```

---

### US-15 : Inscription d'un prospect
> **En tant que** prospect  
> **Je veux** créer un compte avec mon pseudo, adresse email et mot de passe  
> **Afin de** devenir membre et débloquer les achats, ventes et échanges.

* **Endpoint :** `POST /api/v1/auth/register`
* **Headers :** `Content-Type: application/json`

#### Request Body
```json
{
  "pseudo": "Gamer123",
  "email": "gamer123@example.com",
  "password": "PasswordSecure99!"
}
```

#### Responses
* **`201 Created`** : Compte créé et session démarrée
  ```json
  {
    "token": "jwt_token_string",
    "user": USER
  }
  ```
* **`409 Conflict`** : Pseudo ou adresse email déjà utilisé
  ```json
  {User or Email all ready use}
  ```
* **`406 Not acceptable`** : mot de passe non correct
  ```json
  {Error mdp}
  ```
  
  ### US-16 :  [WebSocket] Notification lors d'une vente
> **En tant que** utilisateur
> **Je veux** etre prévenu quand une de mes cartes mises en vente est vendue
> **Afin d'etre informé du montant à laquelle elle a été vendu et ce que j'ai en crypto sur mon compte.


> [!NOTE] Title
> Se renseigner avec le k sur la mise en place


### US-17 : Consultation des cartes personnelles en vente sur le marché
> **En tant qu'** utilisateur connecté  
> **Je veux** consulter la liste de mes propres cartes actuellement en vente sur le marché  
> **Afin de** suivre mes offres en cours et vérifier si elles sont toujours disponibles.

- **Endpoint :** `GET /api/v1/market/my-listings`
- **Headers :** `Authorization: Bearer <token>`
- **Query Parameters :**
  - `page` *(int, default: 0)* : Numéro de page (par tranches de 10)
  - `limit`

#### Request Body
```json
{
  "pseudo": "Gamer123",
  "email": "gamer123@example.com",
  "password": "PasswordSecure99!"
}
```

#### Responses
* **`200 `** : Compte modifié
  ```json
  {
    "token": "jwt_token_string",
    "user": USER
  }
  ```
* **`409 Conflict`** : Pseudo ou adresse email déjà utilisé
  ```json
  {User or Email all ready use}
  ```
* **`406 Not acceptable`** : mot de passe non correct
  ```json
  {Error mdp}
  ```

### US-18 : Modifier le password ou le pseudo 
> **En tant qu'** utilisateur connecté  
> **Je veux** modifier mon mdp ou mon pseudo 
> **Afin de** modifier si jén ai envie 

- **Endpoint :** `POST /api/v1/param/`
- **Headers :** `Authorization: Bearer <token>`

#### Responses
- **`200 OK`** : 
  ```json
  {
    "page": 0,
    "total_results": 3,
    "items": [
      {
        "card": CARD,
        "card_user": CARD_USER
      }
    ]
  }

- **`401 Unauthorized`** : pas connecté
  ```json
    {Error Unauthorized}
  ```

---
## SYSTEME
### US-19 [Tâche de fond / Cron] : Scraping et génération continue de cartes via IGDB
> **En tant que** système  
> **Je veux** exécuter un script automatique en tâche de fond pour importer un certains nombre de cartes depuis l'API IGDB qui puisse etre réutilisable dans le temps. 
> **Afin d'** enrichir le catalogue continuellement sans le faire manuellement *(je fais des rimte, jespere vous avez la ref)*.

* **Logique métier :**
  1. Appel de l'endpoint IGDB Games avec un offset ou filtre aléatoire.
  2. Extraction du titre, de la franchise, du type de jeu (Main Game, DLC/Expansion) et de la pochette.
  3. Création automatique de l'entrée dans la base avec le schéma <span style="color: #2ecc71; font-weight: bold;">Card</span>.

---
## ADMIN (FAIS PAR IA, OPTIONNEL)
### US-20 : Back-Office Admin — Métriques financières et Top Investisseurs
> **En tant qu'** administrateur unique  
> **Je veux** consulter le volume global de crypto dépensé et la liste décroissante des utilisateurs ayant le plus investi  
> **Afin de** piloter la santé financière et identifier les plus gros clients (*whales*).

* **Endpoint :** `GET /api/v1/admin/analytics/investors`
* **Headers :** `Authorization: Bearer <admin_token>`
* **Query Parameters :**
  * `limit` *(int, default: 20)*
  * `order` *(enum: desc, default: desc)*

#### Responses
* **`200 OK`** : Données financières et classement
  ```json
  {
    "financial_summary": {
      "total_crypto_injected": 154200.50,
      "total_packs_sold": 3410,
      "total_marketplace_fees": 4510.20
    },
    "top_investors": [
      {
        "rank": 1,
        "user_id": "uuid | int",
        "pseudo": "WhaleMaster",
        "total_crypto_spent": 12500.00,
        "cards_owned_count": 450,
        "registered_at": "2026-01-10T08:00:00Z"
      },
      {
        "rank": 2,
        "user_id": "uuid | int",
        "pseudo": "CollectorPro",
        "total_crypto_spent": 8400.00,
        "cards_owned_count": 310,
        "registered_at": "2026-03-22T11:15:00Z"
      }
    ]
  }
  ```
* **`403 Forbidden`** : Accès refusé (compte non administrateur)
  ```json
  <span style="color: #2ecc71; font-weight: bold;">ErrorResponse</span>
  ```


---

## Template  US


```markdown
### US-XX : [Titre de la fonctionnalité]
> **En tant qu'** [rôle]  
> **Je veux** [action]  
> **Afin de** [bénéfice attendu]

* **Endpoint :** `METHOD /chemin`
* **Headers :** `...`
* **Query Parameters :** *(Optionnel)*
  * `param_nom` *(type, default)* : description
```
#### Request Body *(Optionnel)*
```json
{
  "champ": "type"
}
```
#### Responses
* **`200 OK`** : Succès
  ```json
  {
    "item": Card
  }
  ```
* **`401 Unauthorized`** :
  ```json
  {ErrorResponse}
  ```
  