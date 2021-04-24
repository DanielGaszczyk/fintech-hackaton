from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from resources import UserLogin, UserRegister

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
api = Api(app)

api.add_resource()
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogin, '/register')