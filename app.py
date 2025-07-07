from flask import Flask, redirect, url_for, session, request
try:
    import flask_session
    print("✅ Flask-Session is installed.")
except ImportError:
    print("❌ Flask-Session is missing.")
from flask_session import Session
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
from datetime import datetime
import os
import logging

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ["APP_SECRET_KEY"]

# Configure server-side sessions to prevent CSRF mismatch
app.session_cookie_name = app.config.get("SESSION_COOKIE_NAME", "session")
app.config.update(
    SESSION_TYPE='filesystem',
    SESSION_PERMANENT=False,
    SESSION_USE_SIGNER=True,
    SESSION_FILE_DIR='/tmp/flask_session/',
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=False  # Set to True in production (HTTPS)
)
Session(app)

# Setup structured logging (to terminal and optionally to file)
logging.basicConfig(level=logging.INFO)
handler = logging.FileHandler("appdebug.log")  # Optional: log to file
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# Register Auth0 OAuth
oauth = OAuth(app)
auth0 = oauth.register(
    'auth0',
    client_id=os.environ["AUTH0_CLIENT_ID"],
    client_secret=os.environ["AUTH0_CLIENT_SECRET"],
    api_base_url="https://" + os.environ["AUTH0_DOMAIN"],
    access_token_url="https://" + os.environ["AUTH0_DOMAIN"] + "/oauth/token",
    authorize_url="https://" + os.environ["AUTH0_DOMAIN"] + "/authorize",
    client_kwargs={'scope': 'openid profile email'},
    server_metadata_url=f"https://{os.environ['AUTH0_DOMAIN']}/.well-known/openid-configuration"
)

@app.route('/')
def home():
    return 'Welcome!!!!! <a href="/login">Login</a>'

@app.route('/login')
def login():
    return auth0.authorize_redirect(redirect_uri=os.environ["AUTH0_CALLBACK_URL"])

@app.route('/callback')
def callback():
    try:
        token = auth0.authorize_access_token()
        userinfo = token['userinfo']
        session['user'] = userinfo

        # ✅ Log successful login
        app.logger.info({
            "event": "user_login",
            "user_id": userinfo.get("sub"),
            "email": userinfo.get("email"),
            "timestamp": datetime.utcnow().isoformat()
        })

        return redirect('/dashboard')
    except Exception as e:
        app.logger.error(f"[callback error] {e}")
        return "Login failed. Check server logs.", 500

@app.route('/dashboard')
def dashboard():
    user = session.get('user')
    if not user:
        return redirect(url_for('login'))
    return f"Hello, {user['name']}! <a href='/logout'>Logout</a>"

@app.route('/protected')
def protected():
    if 'user' not in session:
        # ✅ Log unauthorized access
        app.logger.warning({
            "event": "unauthorized_access",
            "path": request.path,
            "timestamp": datetime.utcnow().isoformat()
        })
        return redirect(url_for('login'))

    # ✅ Log valid access to protected route
    user = session['user']
    app.logger.info({
        "event": "protected_access",
        "user_id": user.get("sub"),
        "email": user.get("email"),
        "timestamp": datetime.utcnow().isoformat()
    })
    return f"Welcome to the protected page, {user['name']}!"

@app.route('/logout')
def logout():
    session.clear()
    return redirect(f"https://{os.environ['AUTH0_DOMAIN']}/v2/logout?" +
                    f"returnTo={url_for('home', _external=True)}&client_id={os.environ['AUTH0_CLIENT_ID']}")

