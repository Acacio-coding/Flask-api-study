import os
from os import path

from dotenv import find_dotenv, load_dotenv
from flask import Flask

from .database import db


def create_app():
    load_dotenv(find_dotenv())
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ["SECRET_KEY"],
        SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URI"),
        SQLALCHEMY_TRACK_MODIFICATIONS = False 
    )

    db.app = app
    db.init_app(app)
    create_database(app)

    return app

def create_database(app):
    if not path.exists(os.environ.get("DATABASE_PATH")):
        db.create_all(app=app)
