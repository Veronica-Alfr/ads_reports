from flask import Flask
from .routes.platforms import platforms_bp
from .routes.accounts import accounts_bp
from .routes.fields import fields_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(platforms_bp)
    app.register_blueprint(accounts_bp)
    app.register_blueprint(fields_bp)

    return app
