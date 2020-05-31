from flask_restful import Resource
from models.item import ItemModel
from schemas.item import ItemSchema

item_schema = ItemSchema()
item_list_schema = ItemSchema(many=True)


class Status(Resource):
    @classmethod
    def get(cls, name):
        ItemModel.best_status(name)
        return {'message': 'Is Ok.'}, 200

        # if item:
        #     return item_schema.dump(item), 200
        # return {'message': 'Item not found.'}, 404
