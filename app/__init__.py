from posix import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    connection_string = os.environ.get("DEVELOPMENT_CONNECTIONSTRING") if not test_config else os.environ.get("TEST_CONNECTIONSTRING")

    app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if test_config:
        app.config["TESTING"]

    migrate.init_app(app, db)
    from app.recipe.Recipe import Recipe

    db.init_app(app)

    from .routes import recipe_bp
    app.register_blueprint(recipe_bp)

    return app