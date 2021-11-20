
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        from .auth import auth
        app.register_blueprint(auth, url_prefix="/")

        from .models import Users
        return app


