import os

from dotenv import find_dotenv, load_dotenv
from flask import Flask


def create_app():
    load_dotenv(find_dotenv())
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = os.environ["SECRET_KEY"] 
    )

    return app
