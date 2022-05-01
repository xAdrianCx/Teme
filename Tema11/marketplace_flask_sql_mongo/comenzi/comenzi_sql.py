from datetime import datetime
from pytz import country_timezones, timezone
from baza_de_date.sql import SQLiteDatabaseConnection
from common.utils import genereaza_id
from baza_de_date.sql_models.orders_sql_db_model import OrdersSQLDBModel


def list_order_flask_sql(id_comanda):
    db = SQLiteDatabaseConnection()
    with db:
        order = db.get_order_by_id(id_comanda)
        if not order:
            return 404, f"Order with ID: {id_comanda} doesn't exist in database."
        order = order.serialize()
    return 200, order


def create_order_flask_sql(request_body):
    db = SQLiteDatabaseConnection()
    id_comanda = genereaza_id({request_body["order_name"]: request_body["order_quantity"]})
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
    request_body["id_comanda"] = id_comanda
    request_body["data_inregistrare"] = data_inregistrare
    order_model = OrdersSQLDBModel(**request_body)
    with db:
        id_comanda = db.create_order(order_model)
    return 201, f"Order: {id_comanda} has been successfully created."


def list_all_orders_flask_sql():
    db = SQLiteDatabaseConnection()
    with db:
        orders_list = OrdersSQLDBModel.serialize_list(db.list_all_orders())
        if not orders_list:
            return 404, "There are no orders in database."
    return 200, orders_list


def delete_order_flask_sql(id_comanda):
    db = SQLiteDatabaseConnection()
    with db:
        rows = db.delete_order_by_id(id_comanda)
    if rows == 0:
        return 404, f"Order with ID: {id_comanda} doesn't exist in database."
    return 200, f"Successfully deleted order: {id_comanda}."