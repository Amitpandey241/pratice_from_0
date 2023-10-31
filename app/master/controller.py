from app import mongo

def check_user(email):
    try:
        result = mongo.db.user_detail.find_one({"email":email})
        if result:
            return True
        else:
            return False
    except Exception as error:
        return str(error)

def insert_into_user_detail(details):
    try:
        obj = {**details}
        result = mongo.db.user_detail.insert_one(obj)
        if result.acknowledged:
            return True
        else:
            return False
    except Exception as error:
        return str(error)
# print(insert_into_user_detail({"name":"amit"}))

def get_all_product():
    result = list(mongo.db.product.find({}))
    if result:
        return result

def get_product_byid(id):
    try:
        result = mongo.db.product.find_one({"_id":id},{})
        print(result)
        return result
    except Exception as error:
        return str(error)
# print(get_product_byid(1))
def insert_new_product(detials):
    try:
        result = mongo.db.product.insert_one({**detials})
        if result.acknowledged:
            return result.acknowledged
        else:
            return False
    except Exception as error:
        return str(error)
def update_product(id,details):
    try:
        result = mongo.db.product.update_one({"_id":id},[{"$set":{**details}}])
        if result.acknowledged:
            return result.acknowledged
        else:
            return False
    except Exception as error:
        return str(error)
def delete_one(id):
    try:
        result = mongo.db.product.delete_one({"_id":id})
        if result.acknowledged:
            return result.acknowledged
        else:
            return False
    except Exception as error:
        return str(error)