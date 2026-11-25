from authlib.integrations.starlette_client import OAuth
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
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

oauth.register( # Register the remote application
    name='github',
    client_id=os.environ["GITHUB_CLIENT_ID"],
    client_secret=os.environ["GITHUB_CLIENT_SECRET"],
    access_token_url='https://github.com/login/oauth/access_token', # Authorization Server called by my server (Back Channel).
    authorize_url='https://github.com/login/oauth/authorize', # Authorization Server called by the browser (Front Channel).
    api_base_url='https://api.github.com/', # Resource Server called by my server.
    client_kwargs={'scope': 'user:email'},
)

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ["SESSION_SECRET"], session_cookie="oauth_state")

@app.get('/login/github') # Génère un State, le stock dans un cookie de session et repond par une redirection.
async def login_github(request: Request):
    redirect_uri = request.url_for('github_callback') 
    return await oauth.github.authorize_redirect(request, redirect_uri)

@app.get('/auth/github')
async def github_callback(request: Request):
    token = await oauth.github.authorize_access_token(request)
    resp = await oauth.github.get("user", token=token)
    resp.raise_for_status()
    return resp.json()
    # user = token['userinfo']
    # return dict(user)
