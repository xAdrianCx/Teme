import json

from flask import Flask, Response, request
from baza_de_date.functii import citeste_datele_din_baza_de_date
from utilizatori.functii import adauga_un_utilizator_flask, listeaza_toti_utilizatorii_flask, sterge_un_utilizator_flask
from comenzi.functii import adauga_o_comanda_flask, modifica_comanda_flask, listeaza_toate_comenzile_flask, sterge_o_comanda_flask
from produse.functii import adauga_un_produs_flask, listeaza_toate_produsele_flask, sterge_produs_flask

app = Flask("Marketplace API")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> USERS FUNCTIONS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


@app.route("/get_user/<string:user_id>", methods=["GET"])
def get_user(user_id):
    users = listeaza_toti_utilizatorii_flask()
    try:
        return Response(status=200, response=json.dumps({"Message:" f"Hello, I'm A user: {users[user_id]}"}))
    except KeyError:
        return Response(status=404, response=json.dumps({"Message:" f"Nu am gasit userul cu ID: {user_id}"}))


@app.route("/add_user", methods=["POST"])
def add_user():
    message = json.loads(request.data)
    user_name = message.get("user_name")
    email_address = message.get("email_address")
    if not user_name or not email_address:
        return Response(status=500, response=json.dumps({"Message": "user_name or email_address is missing"}))
    if len(user_name) < 1 or len(user_name) > 50:
        return Response(status=500, response=json.dumps(
            {"message": "user_name must be longer than 1 character and less than 50 characters"}))
    id_utilizator = adauga_un_utilizator_flask(user_name, email_address)
    return Response(status=200, response=json.dumps({"Message": f"User with ID: {id_utilizator} has been successfully added."}))


@app.route("/list_users", methods=["GET"])
def list_users():
    response = listeaza_toti_utilizatorii_flask()
    print(response)
    return Response(status=200, response=json.dumps(listeaza_toti_utilizatorii_flask()))


@app.route("/delete_user/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    status, message = sterge_un_utilizator_flask(user_id)
    return Response(status=status, response=json.dumps({"Message": message}))


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ORDERS FUNCTIONS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


@app.route("/add_new_order", methods=["POST"])
def add_new_order():
    message = json.loads(request.data)
    order_details = {}
    for key, value in message.items():
        if len(key) < 2 or len(key) > 50 or key == "" or key == None:
            return Response(status=406, response=json.dumps(
                {"Message": f"The name of a product {key} isn't " +
                            "between 1 and 50 characters long, so it won't be added."}))
        elif value == None or value == "":
            return Response(status=404, response=json.dumps({
                "Message": f"Quantity is missing for {key}."}))
        else:
            if (len(key) > 1 and len(key) < 50) and (value != None or value != ""):
                order_details[key] = value
    id_comanda = adauga_o_comanda_flask(order_details)
    return Response(status=200, response=json.dumps({
        "Message": f"Order with ID: {id_comanda} has been successfully added."}))


@app.route("/order_modify/<string:order_id>/<string:option>", methods=["POST"])
def order_modify(order_id, option):
    message = json.loads(request.data)
    product = message.get("product")
    quantity = message.get("quantity")
    date = citeste_datele_din_baza_de_date()
    if order_id in date["comenzi"]:
        if option == "a":
            return Response(status=200, response=json.dumps({
                "Message:" "To the order with ID:" +
                f" {modifica_comanda_flask(order_id, option, product, quantity)}," +
                f" we successfully added the product '{product}' with quantity of {quantity}."}))
        elif option == "m":
            return Response(status=200, response=json.dumps({
                "Message:" "To the order with ID:" +
                f" {modifica_comanda_flask(order_id, option, product, quantity)}," +
                f" we successfully modified the quantity of the product '{product}'" +
                f" to {quantity}."}))
        elif option == "s":
            return Response(status=200, response=json.dumps({
                "Message:" "From the order with ID:" +
                f" {modifica_comanda_flask(order_id, option, product, quantity)}," +
                f" we successfully deleted the product '{product}'."}))
        elif option not in ["a", "m", "s"]:
            return Response(status=404, response=json.dumps({"Message:" f"The option {option} doesn't exist."}))
    elif order_id not in date["comenzi"]:
        return Response(status=404, response=json.dumps({"Message:" f"The order with ID: {order_id} couldn't be found."}))


@app.route("/list_all_orders", methods=["GET"])
def list_all_orders():
    response = listeaza_toate_comenzile_flask()
    return Response(status=200, response=json.dumps(response))


@app.route("/delete_order/<string:order_id>", methods=["DELETE"])
def delete_order(order_id):
    status, message = sterge_o_comanda_flask(order_id)
    return Response(status=status, response=json.dumps({"Message": message}))


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PRODUCTS FUNCTIONS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


@app.route("/add_product", methods=["POST"])
def add_product():
    message = json.loads(request.data)
    product = message.get("product")
    price = message.get("price")
    if not product or not price:
        return Response(status=404, response=json.dumps({"Message": "Product or price is missing."}))
    if len(product) < 1 or len(product) > 50:
        return Response(status=500, response=json.dumps({
            "Message": "Product must be between 1 and 50 characters long."}))
    product_id = adauga_un_produs_flask(product, price)
    return Response(status=200, response=json.dumps({
        "Message": f"Product with ID: {product_id} has been successfully created."}))


@app.route("/list_all_products", methods=["GET"])
def list_all_products():
    products = listeaza_toate_produsele_flask()
    if products:
        return Response(status=200, response=json.dumps({"Message": products}))
    else:
        return Response(status=404, response=json.dumps({"Message": "There are no products in the database just yet."}))


@app.route("/delete_product/<product_id>", methods=["DELETE"])
def delete_product(product_id):
    status, message = sterge_produs_flask(product_id)
    return Response(status=status, response=json.dumps({"Message": message}))


if __name__ == "__main__":
    app.run()
