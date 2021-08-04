from flask import Flask

app = Flask(__name__,template_folder='templates')

from socialcomapnyblog.Core.view import core
from socialcomapnyblog.Error_pages.handlers import error_page

app.register_blueprint(core)
app.register_blueprint(error_page)