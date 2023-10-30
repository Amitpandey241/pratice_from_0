from flask import Blueprint,make_response,jsonify,request
from flask_restful import Resource,Api
from app import app,api
from app.master.controller  import check_user,insert_into_user_detail

blu = Blueprint("blu",__name__)

class RegisterUser(Resource):
    def post(self):
        try:
            email = request.json.get("email")
            first_name = request.json.get("first_name")
            last_name = request.json.get("last_name")
            password = request.json.get("password")
            details = {"email":email,"first_name":first_name,"last_name":last_name,"password":password}
            if email in [None," ",""] and first_name in [None," ",""] and last_name in [None," ",""] and password in [None," ",""]:
                return jsonify({"error":"Please Fill all the fields!!!"})
            else:
                result = check_user(email)
                if result:
                    return jsonify({"msg": "You are al ready register!"})
                else:
                    insert_status = insert_into_user_detail(details)
                    status_msg = "User Register Sucessfully!" if insert_status else "Check the enterd details"
                    return jsonify({"msg":status_msg})

        except Exception as error:
            return jsonify({"msg":str(error)})
class Product(Resource):
    def
api.add_resource(RegisterUser, "/register/")