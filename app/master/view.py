from flask import Blueprint,make_response,jsonify,request
from flask_restful import Resource,Api
from app import app,api
from controller import check_user
blu = Blueprint("blu",__name__)

class RegisterUser(Resource):
    def post(self):
        try:
            email = request.json.get("email")
            first_name = request.json.get("first_name")
            last_name = request.json.get("last_name")
            password = request.json.get("password")

            if email in [None," ",""] and first_name in [None," ",""] and last_name in [None," ",""] and password in [None," ",""]:
                return jsonify({"error":"Please Fill all the fields!!!"})
            else:
                result = check_user(email)
                if result:

