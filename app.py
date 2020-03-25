import os

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
jwt_manager = JWTManager()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db" if os.environ.get(
        "FLASK_ENV") == "development" else os.environ.get(
        "DATABASE_URL")
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    jwt_manager.init_app(app)
    from server.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app
