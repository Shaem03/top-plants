import logging

from flask import Flask
from flask_cors import CORS

from server.config import config
from server.view.controllers import mod_api
from server.view.errors import errors
from server.view.models import db, ma


def create_app():
    """For to use dynamic environment"""
    app = Flask(__name__, instance_relative_config=True)
    cors = CORS(app, resources={r"/api/*": {"origins": "*", "allow_headers": "*", "expose_headers": "*"}})

    app.config.from_object(config["api"])
    logging.getLogger('flask_cors').level = logging.DEBUG

    app.app_context().push()
    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(mod_api)
    app.register_blueprint(errors)

    app.app_context().push()

    return app


application = create_app()

if __name__ == '__main__':
    application.run()
