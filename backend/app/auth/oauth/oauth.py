from authlib.integrations.starlette_client import OAuth
from fastapi import APIRouter, FastAPI, requests
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
# from app.auth.auth import
import os

'''
Étapes :
1- Le Client demande l'autorisation au Authorization Server
2- L'Authorization Server lui renvoit un token
3- Le Client donne ce token au Resource Server
4- Le Resource Server lui donne les ressources
5- Le Client check si le User existe déjà dans la DB
6- S'il existe il est authentifié
7- S'il n'existe pas il est créé
'''

oauth = OAuth() # Crée un objet OAuth() -->

oauth.register( # Resister the remote application
    name='github',
    client_id=os.environ["GIT-HUB-CLIENT-ID"],
    client_secret=os.environ["GIT-HUB-CLIENT-SECRET"],
    access_token_url='https://github.com/login/oauth/access_token',
    # access_token_params='None',
    authorize_url='https://github.com/login/oauth/authorize',
    # authorize_params='None',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="some-random-key")

@app.get('/login/github')
async def login_via_github(request: Request): # Prend la requette en arg, crée un client et lui envoie la requette pour avoir un token en retour.
    # github = oauth.create_client('github')
    # redirect_uri = 'https://example.com/authorize'
    redirect_uri = request.url_for('login_via_github')
    # return await github.authorize_redirect(request, redirect_uri)
    return await oauth.authorize_redirect(request, redirect_uri)

@app.get('/auth/github')
async def authorize(request: Request):
    token = await oauth.github.authorize_access_token(request)
    # resp = oauth.github.get('user', token=token)
    # resp.raise_for_status()
    # profil = resp.json()
    user = token['userinfo']
    return dict(user)
