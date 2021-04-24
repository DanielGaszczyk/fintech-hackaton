from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://nfyruqzhrxbskr:2d41d8b59c3ae060bc8adb06a061bd7fa9df87067ad33c13928cdad1f0b6bfd0@ec2-34-247-118-233.eu-west-1.compute.amazonaws.com:5432/d53f2ibtb5gc8l"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
api = Api(app)
