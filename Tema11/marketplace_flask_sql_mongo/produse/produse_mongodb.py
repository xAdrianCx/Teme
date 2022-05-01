from baza_de_date.mongo_models.mongo_db import MongoDB
from datetime import datetime
from pytz import country_timezones, timezone
from common.utils import genereaza_id
from baza_de_date.mongo_models.products_mongo_db_model import ProductsMongoDBModel


def create_product_flask_mongo(request_body):
    db = MongoDB()
    if not request_body["product"] or not request_body["price"]:
        return 404, f"Product or price is missing."
    if len(request_body["product"]) < 1 or len(request_body["product"]) > 50:
        return 404, f"Product name must be between 1 and 50 characters."
    else:
        id_produs = genereaza_id(request_body["product"])
    if id_produs in db.list_all_ids():
        return 307, f"A product with the same name already exists."
    else:
        data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0])).isoformat()
        request_body["id_produs"] = id_produs
        request_body["data_inregistrare"] = data_inregistrare
        product_model = ProductsMongoDBModel(**request_body)
        id_produs = db.create_product(product_model)
        return 201, f"Product with ID: {id_produs} has been successfully created."


def get_product_flask_mongo(id_produs):
    db = MongoDB()
    product = db.get_product_by_id(id_produs)
    if not product:
        return 404, f"The product with ID: {id_produs} doesn't exist in database."
    return 200, product


def list_all_products_flask_mongo():
    db = MongoDB()
    all_products = db.list_all_products()
    if not all_products:
        return 404, f"There are no products in the database."
    return 200, all_products


def delete_product_by_id_flask_mongo(id_produs):
    db = MongoDB()
    product = db.get_product_by_id(id_produs)
    if not product:
        return 404, f"There is no product: {product} in the database."
    db.delete_product_by_id(id_produs)
    return 200, f"Successfully delete the product: {product}."
