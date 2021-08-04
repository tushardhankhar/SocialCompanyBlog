
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__,template_folder='templates')

basedir = os.path.abspath(os.path.dirname(__file__))

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user.login'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

Migrate(app,db)

from socialcomapnyblog.Core.view import core
from socialcomapnyblog.Error_pages.handlers import error_page

app.register_blueprint(core)
app.register_blueprint(error_page)