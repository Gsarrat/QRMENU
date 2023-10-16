from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import IMAGES, UploadSet, configure_uploads
from flask_bcrypt import Bcrypt
import os
from flask_login import LoginManager
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///gestor.db"
app.config['SECRET_KEY'] = "12345"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from menu_digital.admin import rotas




