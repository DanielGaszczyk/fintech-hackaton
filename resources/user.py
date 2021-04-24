from flask_restful import Resource, reqparse
import hashlib
from models import User

post_user_parser = reqparse.RequestParser()
post_user_parser.add_argument(
    'login',
    required=True,
    location='json'
)
post_user_parser.add_argument(
    'password',
    required=True,
    location='json'
)


class UserLogin(Resource):
    def post(self):
        data = post_user_parser.parse_args()
        hashed_password = hashlib.sha512(data.password.encode('utf-8')).hexdigest()
        user = User.search_for_user(data.login, hashed_password)
        if user is None:
            return {'message': 'user with login {} not found'.format(data.login)}, 404
        else:
            return user.json(), 200


class UserRegister(Resource):
    def post(self):
        data = post_user_parser.parse_args()
        hashed_password = hashlib.sha512(data.password.encode('utf-8')).hexdigest()
        user = User(data.login, hashed_password)
        user.save_to_db()
        return user.json(), 200

