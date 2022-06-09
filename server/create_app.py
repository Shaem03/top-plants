import logging

from flask import Flask
from config import config
from server.api.controllers import mod_api
from server.api.errors import errors
from server.api.models import db, ma


def create_app():
    """For to use dynamic environment"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config["api"])
    logging.getLogger('flask_cors').level = logging.DEBUG
    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(mod_api)
    app.register_blueprint(errors)

    app.app_context().push()

    return app


application = create_app()
application.run()
