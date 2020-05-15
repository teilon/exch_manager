from flask_restful import Resource
from models.handler import HandlerModel
from schemas.handler import HandlerSchema

handler_schema = HandlerSchema()
handler_list_schema = HandlerSchema(many=True)


class Handler(Resource):
    @classmethod
    def get(cls, name):
        handler = HandlerModel.find_by_name(name)
        if handler:
            return handler_schema.dump(handler), 200
        return {'message': 'handler not found'}, 404

    @classmethod
    def post(cls, name):
        if HandlerModel.find_by_name(name):
            return {'message': "A Handler with name '{}' already exists.".format(name)}, 400

        handler = HandlerModel(name)
        try:
            handler.save_to_db()
        except:
            return {'message': 'An error occurred while creating the store.'}, 500

        return handler_schema.dump(handler), 201

    @classmethod
    def delete(cls, name):
        handler = HandlerModel.find_by_name(name)
        if handler:
            handler.delete_from_db()
        return {'message': "Handler '{}' deleted.".format(name)}


class HandlerList(Resource):
    @classmethod
    def get(cls):
        return {'handlers': handler_list_schema.dump(HandlerModel.find_all())}
