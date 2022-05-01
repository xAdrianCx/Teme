from baza_de_date.mongo_models.mongo_db import MongoDB
from datetime import datetime
from pytz import country_timezones, timezone
from common.utils import genereaza_id
from baza_de_date.mongo_models.orders_mongo_db_model import OrdersMongoDBModel

def listeaza_comanda_flask_mongo(id_comanda):
    db = MongoDB()
    order = db.get_order_by_id(id_comanda)
    if not order:
        return 404, f"Comanda cu id: {id_comanda} nu se afla in baza de date."
    return 200, order


def adauga_comanda_flask_mongo(request_body):
    db = MongoDB()
    id_comanda = genereaza_id({request_body["order_name"]: request_body["order_quantity"]})
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0])).isoformat()
    request_body["id_comanda"] = id_comanda
    request_body["data_inregistrare"] = data_inregistrare
    order_model = OrdersMongoDBModel(**request_body)
    id_comanda = db.create_order(order_model)
    return 201, f"Order with ID: {id_comanda} has been successfully created."


def listeaza_toate_comenzile_flask_mongo():
    db = MongoDB()
    order_list = db.list_all_orders()
    if not order_list:
        return 404, "Nu exista comenzi."
    return 200, order_list


def sterge_o_comanda_flask_mongo(id_comanda):
    db = MongoDB()
    if not db.get_order_by_id(id_comanda):
        return 404, f"Comanda cu id {id_comanda} nu exista in baza de date."
    db.delete_order_by_id(id_comanda)
    return 200, f"Successfully deleted order with ID: {id_comanda}."
