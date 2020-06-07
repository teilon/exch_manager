from flask import Flask, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from db import db

from db import SQLALCHEMY_DATABASE_URI
from ma import ma
from resources.handler import Handler, HandlerList
from resources.item import Item, ItemList
from resources.status import StatusBestBuy, StatusBestSale

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI # 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

db.init_app(app)
ma.init_app(app)

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):     # except ValidationError as err
    return jsonify(err.messages), 400


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Handler, '/handler/<string:name>')
api.add_resource(HandlerList, '/handlers')
api.add_resource(StatusBestBuy, '/status/buy/<string:name>')
api.add_resource(StatusBestSale, '/status/sale/<string:name>')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
