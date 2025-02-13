from flask import Flask
from .routes.root import root_bp
from .routes.api import api_bp
from .routes.reports_platform import reports_platform_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(root_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(reports_platform_bp)

    return app
