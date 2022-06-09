from app import db, metadata, ma
from sqlalchemy import Table, PrimaryKeyConstraint


class EGridPlant(db.Model):
    __table_args__ = (
        PrimaryKeyConstraint('seqplt20'),
    )

    seq_number = db.Column("seqplt20", db.BIGINT)

    state_abbr = db.Column("pstatabb", db.TEXT)

    plant_name = db.Column("pname", db.TEXT)

    owner_name = db.Column("oprname", db.TEXT)

    owner_id = db.Column("oprcode", db.TEXT)

    utility_name = db.Column("utlsrvnm", db.TEXT)

    utility_id = db.Column("utlsrvid", db.BIGINT)

    authority_name = db.Column("baname", db.TEXT)

    sub_region_name = db.Column("srname", db.TEXT)

    county_name = db.Column("cntyname", db.TEXT)

    plant_latitude = db.Column("lat", db.FLOAT)

    plant_longitude = db.Column("lon", db.FLOAT)

    num_units = db.Column("numunt", db.BIGINT)

    num_generators = db.Column("numgen", db.BIGINT)

    fuel_category = db.Column("plfuelct", db.TEXT)

    annual_net_generation = db.Column("plngenan", db.TEXT)

    gas_generation_percent = db.Column("plgspr", db.TEXT)

    nuclear_generation_percent = db.Column("plncpr", db.TEXT)

    total_combustion_percent = db.Column("plcypr", db.TEXT)

    total_non_combustion_percent = db.Column("plcnpr", db.TEXT)

    def __init__(self):
        table_reflection = Table("e_grid_plant", metadata, autoload=True, autoload_with=db.engine)
        attrs = {"__table__": table_reflection}
        e_model = "e_grid_plant", (db.Model,), attrs


class EGridPlantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EGridPlant
        load_instance = True


class NercRegion(db.Model):
    __table_args__ = (
        PrimaryKeyConstraint('nerc'),
    )

    acronym = db.Column("nerc", db.TEXT)
    name = db.Column("nercname", db.TEXT)

    def __init__(self):
        table_reflection = Table("nerc_region", metadata, autoload=True, autoload_with=db.engine)
        attrs = {"__table__": table_reflection}
        e_model = "nerc_region", (db.Model,), attrs


class NercRegionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = NercRegion
        load_instance = True
