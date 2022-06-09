from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from config import config

db = SQLAlchemy()
metadata = MetaData()
ma = Marshmallow()


def create_app():
    """For to use dynamic environment"""
    app = Flask(__name__)
    cors = CORS(app)

    app.config.from_object(config["api"])
    db.init_app(app)
    ma.init_app(app)

    from api.controllers import mod_api
    from api.errors import errors

    app.register_blueprint(mod_api)
    app.register_blueprint(errors)

    return app
