from flask_restful import Resource,Api
from flask import Flask, request, jsonify,Blueprint
from flask_pymongo import PyMongo


app = Flask(__name__)
api = Api(app)

app.config["MONGO_URI"] = "mongodb://localhost:27017/Users"
mongo = PyMongo(app)
