from authlib.integrations.starlette_client import OAuth

oauth = OAuth()
# github = oauth.register('github', {...})
oauth.register(
    name='github',
    client_id='{{ your-github-client-id }}',
    client_secret='{{ your-github-client-secret }}',
    acces_token_url='https://github.com/login/oauth/access_token',
    acces_token_params='None',
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params='None',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:mail'},
)

def login(request):
    github = oauth.create_client('github')
    redirect_uri = 'https://example.com/authorize'
    return github.authorize_redirect(request, redirect_uri)

def authorize(request):
    token = oauth.github.authorize_acces_token(request)
    resp = oauth.github.get('user', token=token)
    resp.raise_for_status()
    profil = resp.json()

# @app.route('/login')
# def login():
#     return github.authorize_redirect(url_for('authorize', _external=True))