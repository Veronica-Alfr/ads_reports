from flask import Flask
from .routes.root import root_bp
from .routes.api import api_bp
from .routes.each_report import reports_platform_bp
from .routes.general_reports import general_reports_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(root_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(reports_platform_bp)
    app.register_blueprint(general_reports_bp, url_prefix='/geral')

    return app
