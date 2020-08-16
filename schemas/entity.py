from ma import ma
from models.entity import EntityModel
from schemas.item import ItemModel
from schemas.item import ItemSchema


class EntitySchema(ma.SQLAlchemyAutoSchema):
    items = ma.Nested(ItemSchema, many=True)

    class Meta:
        model = EntityModel
        dump_only = ('id',)
        include_fk = True
        load_instance = True
