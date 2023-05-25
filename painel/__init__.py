
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://michael:xbX3XAEcWnJRroa6nt3ECXlfzWlFArJ0@dpg-chnbj11mbg5577kjht10-a.oregon-postgres.render.com/banco_cvu7'
app.config["SECRET_KEY"] = "b7fb527958e00800faaea98f67a7813d"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from painel.home import home_routes
from painel.auth import auth_routes
