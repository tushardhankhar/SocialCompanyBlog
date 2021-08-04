from flask import Blueprint , render_template

error_page = Blueprint('error_page',__name__)

@error_page.app_errorhandler(404)
def error_404(error):
    return render_template ('error/404.html') , 404

@error_page.app_errorhandler(403)
def error_403(error):
    return render_template ('error/403.html') , 403