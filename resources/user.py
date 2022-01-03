from flask_restful import Resource
from flask import request
from models.user import UserModel
from schemas.user import UserSchema
import bcrypt

from constants import (
    USER_NOT_FOUND,
    USER_DELETED,
    SUCCESSFULLY_AUTORIZED,
    INVALID_CREDENTIALS,
    PW_DO_NOT_MATCH,
    USER_ALREADY_EXISTS,
    CREATED_SUCCESSFULLY
)
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


class UserRegister(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        user = user_schema.load(user_json)
        if user_json['password'] != user_json.get('password1', None):
            return {'message': PW_DO_NOT_MATCH}, 400
        user.password = bcrypt.hashpw(user.password.encode(encoding='UTF-8'), bcrypt.gensalt())

        if UserModel.get_user_by_email(user.email):
            return {'message': USER_ALREADY_EXISTS}, 400
        user.save_to_db()

        return {'message': CREATED_SUCCESSFULLY}, 201


class UserLogin(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        user_data = user_schema.load(user_json)
        user = UserModel.get_user_by_email(user_data.email)
        if user and bcrypt.checkpw(user_data.password.encode(encoding='UTF-8'), user.password):
            return {'message': SUCCESSFULLY_AUTORIZED}, 200
        return {"message": INVALID_CREDENTIALS}, 401
