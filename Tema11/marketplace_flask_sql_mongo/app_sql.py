import json
from flask import Flask, Response, request
from utilizatori.utilizatori_sql import (listeaza_utilizator_flask_sql, adauga_un_utilizator_flask_sql,
                                         listeaza_toti_utilizatorii_flask_sql, sterge_un_utilizator_flask_sql)
from comenzi.comenzi_sql import *
from produse.produse_sql import *

from baza_de_date.sql import SQLiteDatabaseConnection

app = Flask("Marketplace API")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> USERS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@app.route("/get_user/<string:user_id>", methods=["GET"])
def get_user(user_id):
    status, message = listeaza_utilizator_flask_sql(user_id)
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
    status, message = adauga_un_utilizator_flask_sql(request_body)
    return Response(status=status, response=json.dumps(message))


@app.route("/list_users", methods=["GET"])
def list_users():
    status, message = listeaza_toti_utilizatorii_flask_sql()
    return Response(status=status, response=json.dumps(message))


@app.route("/delete_user/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    status, message = sterge_un_utilizator_flask_sql(user_id)
    return Response(status=status, response=json.dumps({message}))


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ORDERS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@app.route("/put_order", methods=["POST"])
def put_order():
    request_body = json.loads(request.data)
    order_name = request_body["order_name"]
    order_quantity = request_body["order_quantity"]
    if not order_name or not order_quantity:
        return Response(status=500, response=json.dumps("order_name or order_quantity is missing."))
    if len(order_name) < 1 or len(order_name) > 50:
        return Response(status=500, response=json.dumps("order_name must be between 1 and 50 characters."))
    status, message = create_order_flask_sql(request_body)
    return Response(status=status, response=json.dumps({"Message": message}))


@app.route("/list_order/<string:order_id>", methods=["GET"])
def list_order(order_id):
    status, message = list_order_flask_sql(order_id)
    return Response(status=status, response=json.dumps(message))


@app.route("/list_all_orders", methods=["GET"])
def list_all_orders():
    status, message = list_all_orders_flask_sql()
    return Response(status=status, response=json.dumps(message))


@app.route("/delete_order/<string:order_id>", methods=["DELETE"])
def delete_order(order_id):
    status, message = delete_order_flask_sql(order_id)
    return Response(status=status, response=json.dumps(message))


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PRODUCTS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@app.route("/put_product", methods=["POST"])
def put_product():
    request_body = json.loads(request.data)
    product_name = request_body["product_name"]
    product_price = request_body["product_price"]
    if not product_name or not product_price:
        return Response(status=500, response=json.dumps("Product_name or product_price is missing."))
    if len(product_name) < 1 or len(product_name) > 50:
        return Response(status=500, response=json.dumps("Product name must be between 1 and 50 characters."))
    status, message = create_product_flask_sql(request_body)
    return Response(status=status, response=json.dumps(message))


@app.route("/list_order/<string:product_id>", methods=["GET"])
def list_product(product_id):
    status, message = list_product_flask_sql(product_id)
    return Response(status=status, response=json.dumps(message))


@app.route("/list_all_products", methods=["GET"])
def list_all_products():
    status, message = list_all_products_flask_sql()
    return Response(status=status, response=json.dumps(message))


@app.route("/delete_product/<string:product_id>", methods=["DELETE"])
def delete_product(product_id):
    status, message = delete_product_flask_sql(product_id)
    return Response(status=status, response=json.dumps(message))


if __name__ == "__main__":
    db = SQLiteDatabaseConnection()
    with db:
        db.create_tables_if_not_exists()
    app.run()
