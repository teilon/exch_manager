from flask_restful import Resource
from models.entity import EntityModel
from schemas.entity import EntitySchema

entity_schema = EntitySchema()
entity_list_schema = EntitySchema(many=True)


class Entity(Resource):
    @classmethod
    def get(cls, name):
        entity = EntityModel.find_by_name(name)
        if entity:
            return entity_schema.dump(entity), 200
        return {'message': 'entity not found'}, 404

    @classmethod
    def post(cls, name):
        if EntityModel.find_by_name(name):
            return {'message': "A Handler with name '{}' already exists.".format(name)}, 400

        entity = EntityModel(name=name)
        try:
            entity.save_to_db()
        except:
            return {'message': 'An error occurred while creating the store.'}, 500

        return entity_schema.dump(entity), 201

    @classmethod
    def delete(cls, name):
        entity = EntityModel.find_by_name(name)
        if entity:
            entity.delete_from_db()
        return {'message': "Handler '{}' deleted.".format(name)}


class EntityList(Resource):
    @classmethod
    def get(cls):
        return {'handlers': entity_list_schema.dump(EntityModel.find_all())}
