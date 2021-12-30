from flask_restful import Resource
from flask import request
from models.user import UserModel
from schemas.user import UserSchema
from marshmallow import ValidationError

from constants import USER_NOT_FOUND, USER_DELETED

user_schema = UserSchema()


class User(Resource):
    def get(self, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': USER_NOT_FOUND}, 404
        return user_schema.dump(user), 200

    @classmethod
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': USER_NOT_FOUND}, 404
        user.delete_user_by_id(user_id)
        return {"message": USER_DELETED}, 200
