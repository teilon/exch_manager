from flask_restful import Resource
from models.item import ItemModel
from schemas.item import ItemSchema

item_schema = ItemSchema()
item_list_schema = ItemSchema(many=True)


class StatusBestBuy(Resource):
    @classmethod
    def get(cls, name):
        item = ItemModel.find_max_buy_price(name)
        if item:
            return item_list_schema.dump(item), 200
        return {'message': 'Item not found.'}, 404


class StatusBestSale(Resource):
    @classmethod
    def get(cls, name):
        item = ItemModel.find_min_sale_price(name)
        if item:
            return item_list_schema.dump(item), 200
        return {'message': 'Item not found.'}, 404