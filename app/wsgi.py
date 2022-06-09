from flask import jsonify, Flask
from flask_cors import cross_origin
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from api.models import NercRegion, NercRegionSchema
from config import config
from run import create_app

db = SQLAlchemy()
metadata = MetaData()
ma = Marshmallow()
application = Flask(__name__)
application.config.from_object(config["api"])
db.init_app(application)
ma.init_app(application)


@application.route("/region")
@cross_origin(origin='*')
def region():
    regions = NercRegion()
    regions_data = regions.query.all()

    region_schema = NercRegionSchema(many=True)
    resp = region_schema.dump(regions_data)
    response = jsonify(
        resp
    ), 200

    return response


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5001)
