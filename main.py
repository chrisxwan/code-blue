"""
CodeBlue app setup
"""


from flask import Flask, g
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import distinct, func
from sqlalchemy.orm import scoped_session, sessionmaker
import os
from flask.ext.login import LoginManager

# Set up app with debugging
app = Flask(__name__)
app.debug = True

# Login manager for authentication.  If not authenticated, route to login page
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'splash.login'

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['YHACK_ADMIN_DATABASE_URL']
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024

db = SQLAlchemy(app)

# for flask-login -- secret key needed to use sessions
# app.secret_key = os.environ['USER_AUTH_SECRET_KEY']

# for S3
app.aws_key = os.environ['CODEBLUE_AWS_ACCESS_KEY_ID']
app.aws_secret = os.environ['CODEBLUE_AWS_SECRET_ACCESS_KEY']
