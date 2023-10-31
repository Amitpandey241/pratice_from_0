from flask import Blueprint,make_response,jsonify,request
from flask_restful import Resource,Api
from app import app,api
from app.master.controller  import check_user,insert_into_user_detail,get_all_product,get_product_byid,insert_new_product,update_product,delete_one

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
    def get(self):
        try:

            get_all =get_all_product()
            if get_all is not []:
                return jsonify({"msg":get_all})
            else:
                return jsonify({"msg":"error while fetching product"})

        except Exception as error:
            return jsonify({"msg":str(error)})

class ProductById(Resource):
    def get(self):
        try:
            id = request.args.get("id")
            print(id)
            get_product = get_product_byid(int(id))
            if get_product is not None:
                return jsonify({"msg":get_product})
            else:
                return jsonify({"msg":"Please check the id"})
        except Exception as error:
            return jsonify({"msg":str(error)})

class AddProduct(Resource):
    def post(self):
        try:

            id = request.json.get("_id")
            name = request.json.get("name")
            des = request.json.get("description")
            stock = request.json.get("stock")

            insert_details = {"_id":id, "name":name, "description":des, "stock": stock}
            status = insert_new_product(insert_details)
            if status:
                return jsonify({"msg":f"Product {name} added sucessfully !"})
            else:
                return jsonify({"msg": "Check the enterd value again!"})

        except Exception as error:
            return jsonify({"msg":str(error)})






api.add_resource(RegisterUser, "/api/register/")
api.add_resource(Product,"/api/products/")
api.add_resource(ProductById,"/api/products/")
api.add_resource(AddProduct,"/api/products/add")

