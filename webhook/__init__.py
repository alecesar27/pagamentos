import sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '29cecf8afd6176f06bb3f55472d490d1'


#if os.getenv('DATABASE_URL'):
#    app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URL')
#else:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webhook.db'
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from webhook import routes
