from flask_restful import Resource, request
from models.user import UserModel
from schemas.user import UserSchema

user_schema = UserSchema()


class UserRegister(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()

        if UserModel.find_by_username(data['username']):
            return {'message': 'A user with that username already exists.'}, 400

        user = user_schema.load(data)
        user.save_to_db()

        return {'message': 'User created successfully'}, 201
