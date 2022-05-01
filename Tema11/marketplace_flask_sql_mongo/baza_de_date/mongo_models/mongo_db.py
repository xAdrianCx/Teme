from pymongo import MongoClient
from urllib import parse
from baza_de_date.mongo_models.users_mongo_db_model import UsersMongoDBModel
from baza_de_date.mongo_models.orders_mongo_db_model import OrdersMongoDBModel
from baza_de_date.mongo_models.products_mongo_db_model import ProductsMongoDBModel
from pathlib import Path
import os
with open(Path(os.path.dirname(os.path.abspath(__file__)), "db_pwd_mongo.txt"), "r") as password_file:
    # connection_url = f"mongodb+srv://test_user:{parse.quote_plus(password_file.readline())}@itf.x5m6f.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    connection_url = f"mongodb+srv://xAdrianCx:{parse.quote_plus(password_file.readline())}@cluster0.55xbt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"


class MongoDB:
    client = MongoClient(connection_url, tls=True, tlsAllowInvalidCertificates=True)
    db = client["a_collection"]
    collection = db["a_table"]

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> USERS METHODS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    def create_user(self, user_model: UsersMongoDBModel):
        print(user_model.__dict__)
        self.collection.insert_one(user_model.__dict__)
        return user_model._id

    def get_user_by_id(self, user_id):
        result = self.collection.find_one({"_id": user_id})
        return result

    def get_user_by_email(self, email):
        result = self.collection.find(filter={"email_address": email})
        return list(result)

    def list_all_users(self):
        result = self.collection.find(filter={"user_name": {"$exists": 1}})
        return list(result)

    def delete_user_by_id(self, user_id):
        self.collection.delete_one({"_id": user_id})

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ORDERS METHODS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    def create_order(self, order_model: OrdersMongoDBModel):
        self.collection.insert_one(order_model.__dict__)
        return order_model._id

    def get_order_by_id(self, order_id):
        order = self.collection.find_one({"_id": order_id})
        return order

    def get_order_by_product(self, product):
        result = self.collection.find(filter={"order_name": product})
        return list(result)

    def list_all_orders(self):
        all_orders = self.collection.find(filter={"order_name": {"$exists": 1}})
        return list(all_orders)

    def delete_order_by_id(self, order_id):
        self.collection.delete_one({"_id": order_id})

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PRODUCTS METHODS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    def create_product(self, product_model: ProductsMongoDBModel):
        self.collection.insert_one(product_model.__dict__)
        return product_model._id

    def get_product_by_id(self, product_id):
        product = self.collection.find_one({"_id": product_id})
        return product

    def list_all_products(self):
        all_products = self.collection.find(filter={"product": {"$exists": 1}})
        return list(all_products)

    def delete_product_by_id(self, product_id):
        self.collection.delete_one({"_id": product_id})

    def list_all_ids(self):
        # A function to return all ids
        # so we can find duplicates without error.
        all_ids = self.collection.find({}, {"_id": 1})
        ids = []
        for i in all_ids:
            for j in i:
                ids.append(i[j])
        return ids
