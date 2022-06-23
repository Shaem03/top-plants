from flask import Blueprint, Response

from server.view.models import db

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(Exception)
def server_error(error):
    return Response(f"Oops, got an error! {error}", status=500)


@errors.teardown_request
def teardown_request(exception):
    if exception:
        db.session.rollback()
    db.session.remove()
