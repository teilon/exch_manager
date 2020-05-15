from ma import ma
from models.handler import HandlerModel
from schemas.item import ItemModel
from schemas.item import ItemSchema


class HandlerSchema(ma.SQLAlchemyAutoSchema):
    items = ma.Nested(ItemSchema, many=True)

    class Meta:
        model = HandlerModel
        dump_only = ('id',)
        include_fk = True
        load_instance = True
