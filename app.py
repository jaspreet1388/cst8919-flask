from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ["APP_SECRET_KEY"]

oauth = OAuth(app)
auth0 = oauth.register(
    'auth0',
    client_id=os.environ["AUTH0_CLIENT_ID"],
    client_secret=os.environ["AUTH0_CLIENT_SECRET"],
    api_base_url=os.environ["AUTH0_DOMAIN"],
    access_token_url=os.environ["AUTH0_DOMAIN"] + "/oauth/token",
    authorize_url=os.environ["AUTH0_DOMAIN"] + "/authorize",
    client_kwargs={'scope': 'openid profile email'},
    server_metadata_url=f"{os.environ['AUTH0_DOMAIN']}/.well-known/openid-configuration",
)

@app.route('/')
def home():
    return 'Welcome! <a href="/login">Login</a>'

@app.route('/login')
def login():
    return auth0.authorize_redirect(redirect_uri=os.environ["AUTH0_CALLBACK_URL"])

@app.route('/callback')
def callback():
    token = auth0.authorize_access_token()
    session['user'] = token['userinfo']
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    return f"Hello, {session['user']['name']}! <a href='/logout'>Logout</a>"

@app.route('/protected')
def protected():
    if 'user' not in session:
        return redirect(url_for('login'))
    return f"Welcome to the protected page, {session['user']['name']}!"

@app.route('/logout')
def logout():
    session.clear()
    return redirect(auth0.api_base_url + "/v2/logout?" +
                    f"returnTo={url_for('home', _external=True)}&client_id={os.environ['AUTH0_CLIENT_ID']}")
