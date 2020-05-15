from ma import ma
from models.item import ItemModel


class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ItemModel
        load_only = ("handler",)
        dump_only = ("id",)
        include_fk = True
        load_instance = True