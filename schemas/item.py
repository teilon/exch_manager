from ma import ma
from marshmallow import EXCLUDE, INCLUDE
from marshmallow import Schema, fields
from models.item import ItemModel


class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ItemModel
        load_only = ("entity",)
        dump_only = ("id",)
        include_fk = True
        load_instance = True
        unknown = EXCLUDE


class ItemSchemaBuy(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ItemModel
        include_fk = True
        exclude = ('entity_id', 'id', 'sale', 'created_date')

    entity_name = ma.Function(lambda field: field.entity.name)


class ItemSchemaSale(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ItemModel
        include_fk = True
        exclude = ('entity_id', 'id', 'buy', 'created_date')

    entity_name = ma.Function(lambda field: field.entity.name)
