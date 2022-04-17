import hashlib
import json
from baza_de_date.functii import citeste_datele_din_baza_de_date, scrie_datele_in_baza_de_date


def genereaza_id(detalii_comanda):
    hash_object = hashlib.md5(bytes(json.dumps(detalii_comanda), encoding='UTF-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def sterge(identificator_de_sters, key):
    datele = citeste_datele_din_baza_de_date()
    if datele[key].get(identificator_de_sters):
        datele[key].pop(identificator_de_sters)
        scrie_datele_in_baza_de_date(datele)
        if key == "utilizatori":
            return 200, f"User with ID: {identificator_de_sters} has been successfully deleted."
        if key == "comenzi":
            return 200, f"Order with ID: {identificator_de_sters} has been successfully deleted."
        if key == "produse":
            return 200, f"Product with ID: {identificator_de_sters} has been successfully deleted."
    elif not datele[key].get(identificator_de_sters):
        if key == "utilizatori":
            return 404, f"User with ID: {identificator_de_sters} does not exist in the database."
        if key == "comenzi":
            return 404, f"Order with ID: {identificator_de_sters} does not exist in the database."
        if key == "comenzi":
            return 404, f"Product with ID: {identificator_de_sters} does not exist in the database."
