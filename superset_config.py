import os
#---------------------------------------------------------
# Superset specific config
#---------------------------------------------------------
# ROW_LIMIT = 5000
SUPERSET_WORKERS = 1 # for it to work in heroku basic/hobby dynos increase as you like

# SUPERSET_WEBSERVER_PORT = 8088
#---------------------------------------------------------

#---------------------------------------------------------
# Flask App Builder configuration
#---------------------------------------------------------
# Your App secret key
SECRET_KEY = '\2\1thisismyscretkey\1\2\e\y\y\h'  # noqa

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# Superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

#---------------------------------------------------------
# Google OAuth configuration
#---------------------------------------------------------
# Following instructions from https://medium.com/@aungmt/superset-with-google-oauth-3ba7a1c1f459

AUTH_TYPE = 'AUTH_OAUTH'
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = 'Public'

OAUTH_PROVIDERS = [
 {
   'name': 'google',
   'whitelist': [os.environ['GOOGLE_OAUTH_DOMAIN']],
   'icon': 'fa-google',
   'token_key': 'access_token',
   'remote_app': {
     'base_url': 'https://www.googleapis.com/oauth2/v2/',
     'request_token_params': {
        'scope': 'email profile'
     },
     'request_token_url': None,
     'access_token_url': 'https://accounts.google.com/o/oauth2/token',
     'authorize_url': 'https://accounts.google.com/o/oauth2/auth',
     'consumer_key': os.environ['GOOGLE_OAUTH_KEY'],
     'consumer_secret': os.environ['GOOGLE_OAUTH_SECRET']
    }
  }
]