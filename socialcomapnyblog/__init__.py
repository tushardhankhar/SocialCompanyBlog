from flask import Flask

app = Flask(__name__,template_folder='templates')

from socialcomapnyblog.Core.view import core

app.register_blueprint(core)