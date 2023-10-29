from app import mongo

def check_user(email):
    try:
        result = mongo.db.user_detail.find_one({"email":email})
        if result:
            return False
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

