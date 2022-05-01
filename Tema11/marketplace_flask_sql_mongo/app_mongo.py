import json
from flask import Flask, Response, request
from utilizatori.utilizatori_mongodb import (adauga_un_utilizator_flask_mongo, listeaza_utilizator_flask_mongo,
                                             listeaza_toti_utilizatorii_flask_mongo, sterge_un_utilizator_flask_mongo)
from comenzi.comenzi_mongodb import *
from produse.produse_mongodb import *

app = Flask("Marketplace API")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> USERS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@app.route("/get_user/<string:user_id>", methods=["GET"])
def get_user(user_id):
    status, message = listeaza_utilizator_flask_mongo(user_id)
    print(message)
    return Response(status=status, response=json.dumps(message))


@app.route("/put_user", methods=["POST"])
def put_user():
    request_body = json.loads(request.data)
    user_name = request_body.get("user_name")
    email_address = request_body.get("email_address")
    if not user_name or not email_address:
        return Response(status=500, response=json.dumps("user_name or email_address is missing"))
    if len(user_name) < 1 or len(user_name) > 50:
        return Response(status=500,
                        response=json.dumps("user_name must be longer than 1 character and less than 50 characters"))
    status, message = adauga_un_utilizator_flask_mongo(request_body)
    return Response(status=status, response=json.dumps(message))


@app.route("/list_users", methods=["GET"])
def list_users():
    status, message = listeaza_toti_utilizatorii_flask_mongo()
    return Response(status=status, response=json.dumps(message))


@app.route("/delete_user/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    status, message = sterge_un_utilizator_flask_mongo(user_id)
    return Response(status=status, response=json.dumps({"message": message}))


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ORDERS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@app.route("/put_order", methods=["POST"])
def put_order():
    request_body = json.loads(request.data)
    order_name = request_body["order_name"]
    order_quantity = request_body["order_quantity"]
    if not order_name or not order_quantity:
        return Response(status=500, response=json.dumps("Product name or quantity is missing."))
    if len(order_name) < 2 or len(order_name) > 50:
        return Response(status=500, response=json.dumps("A product name has to be between 1 and 50 characters"))

    status, message = adauga_comanda_flask_mongo(request_body)
    return Response(status=status, response=json.dumps(message))

@app.route("/get_order/<string:order_id>", methods=["GET"])
def get_order(order_id):
    status, message = listeaza_comanda_flask_mongo(order_id)
    return Response(status=status, response=json.dumps(message))


@app.route("/list_orders", methods=["GET"])
def list_orders():
    status, message = listeaza_toate_comenzile_flask_mongo()
    return Response(status=status, response=json.dumps(message))


@app.route("/delete_order/<string:order_id>", methods=["DELETE"])
def delete_order(order_id):
    status, message = sterge_o_comanda_flask_mongo(order_id)
    return Response(status=status, response=json.dumps({"Message": message}))


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PRODUCTS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
@app.route("/put_product", methods=["POST"])
def put_product():
    request_body = json.loads(request.data)
    product = request_body["product"]
    price = request_body["price"]
    if not product or not price:
        return Response(status=500, response=json.dumps("Product or price is missing."))
    if len(product) < 2 or len(product) > 50:
        return Response(status=500, response=json.dumps("A product name has to be between 1 and 50 characters."))
    status, message = create_product_flask_mongo(request_body)
    return Response(status=status, response=json.dumps({"Message": message}))


@app.route("/get_product/<string:product_id>", methods=["GET"])
def get_product(product_id):
    status, message = get_product_flask_mongo(product_id)
    return Response(status=status, response=json.dumps({"Message": message}))


@app.route("/list_all_products", methods=["GET"])
def list_all_products():
    status, message = list_all_products_flask_mongo()
    return Response(status=status, response=json.dumps({"Message": message}))


@app.route("/delete_product/<string:product_id>", methods=["DELETE"])
def delete_product(product_id):
    status, message = delete_product_by_id_flask_mongo(product_id)
    return Response(status=status, response=json.dumps({"Message": message}))

if __name__ == "__main__":
    app.run()
