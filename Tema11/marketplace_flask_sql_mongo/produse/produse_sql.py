from datetime import datetime
from pytz import country_timezones, timezone
from baza_de_date.sql import SQLiteDatabaseConnection
from common.utils import genereaza_id
from baza_de_date.sql_models.products_sql_db_model import ProductsSQLDBModel


def list_product_flask_sql(id_produs):
    db = SQLiteDatabaseConnection()
    with db:
        product = db.get_product_by_id(id_produs)
        if not product:
            return 404, f"Product with ID: {id_produs} doesn't exist in database."
        product = product.serialize()
    return 200, product


def create_product_flask_sql(request_body):
    db = SQLiteDatabaseConnection()
    with db:
        if not request_body["product_name"] or not request_body["product_price"]:
            return 404, f"Product name or price is missing."
        if len(request_body["product_name"]) < 1 or len(request_body["product_name"]) > 50:
            return 404, f"Product name must be between 1 and 50 characters."
        else:
            id_produs = genereaza_id(request_body['product_name'])
        if request_body['product_name'] in db.list_all_product_names():
            return 307, f"A product with the same name already exists."
        else:
            data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
            request_body['id_produs'] = id_produs
            request_body['data_inregistrare'] = data_inregistrare
            product_model = ProductsSQLDBModel(**request_body)
            id_produs = db.create_product(product_model)
            return 201, f"Product {id_produs} has been successfully created."


def list_all_products_flask_sql():
    db = SQLiteDatabaseConnection()
    with db:
        products = ProductsSQLDBModel.serialize_list(db.list_all_products())
        if not products:
            return 404, "There are no products in the database."
    return 200, products


def delete_product_flask_sql(id_produs):
    db = SQLiteDatabaseConnection()
    with db:
        product_to_delete = db.delete_product_by_id(id_produs)
    if not product_to_delete:
        return 404, f"Product with ID: {id_produs} doesn't exist in database."
    return 200, f"Successfully deleted product {id_produs}."
