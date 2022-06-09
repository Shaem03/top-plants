from flask import Response, jsonify, Blueprint, request
from packaging import _manylinux
from sqlalchemy import desc

from .models import EGridPlant, EGridPlantSchema, NercRegion, NercRegionSchema

mod_api = Blueprint('api', __name__, url_prefix='/api')


@mod_api.route("/")
def index():
    return Response("Welcome!", status=200)


@mod_api.route("/top/<n>")
def top(n):
    egrid = EGridPlant()
    top_plants = egrid.query.order_by(desc(EGridPlant.annual_net_generation)).limit(n).all()

    egrid_schema = EGridPlantSchema(many=True)
    response = egrid_schema.dump(top_plants)
    response = jsonify(
        response
    ), 200
    return response


@mod_api.route("/filter")
def filter_by_region():
    region_abbr = request.args.get('region')
    top_n_arg = request.args.get('top')
    top_n = top_n_arg if top_n_arg else 10
    egrid = EGridPlant()
    if region_abbr:
        filtered_plants = egrid.query.order_by(desc(EGridPlant.annual_net_generation)).filter(
            EGridPlant.state_abbr == region_abbr.upper()).limit(top_n).all()
    else:
        filtered_plants = egrid.query.order_by(desc(EGridPlant.annual_net_generation)).limit(top_n).all()
    egrid_schema = EGridPlantSchema(many=True)
    response = egrid_schema.dump(filtered_plants)
    response = jsonify(
        response
    ), 200
    return response


@mod_api.route("/region")
def region():
    regions = NercRegion()
    regions_data = regions.query.all()

    region_schema = NercRegionSchema(many=True)
    resp = region_schema.dump(regions_data)
    response = jsonify(
        resp
    ), 200
    return response


@mod_api.route("/health")
def health():
    return Response("OK", status=200)