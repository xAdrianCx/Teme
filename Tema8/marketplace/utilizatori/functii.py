"""

Utilizatorii ar trebui sa aiba structura:
("id_utilizator": {
    "nume": "Numele" - string,
    "email": "EmailAddress" - string,
    "data_inregistrare": "DataInregistrare" - string,
})

"""
import hashlib
from datetime import datetime
from baza_de_date.functii import citeste_datele_din_baza_de_date, scrie_datele_in_baza_de_date
from pprint import pprint
from pytz import country_timezones, timezone


def genereaza_id_utilizator(nume, email):
    hash_object = hashlib.md5(bytes(nume + email, encoding='UTF-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def adauga_un_utilizator():
    """
    Introdu de la tastatura cu textul 'Introduceti numele utilizatorului de adaugat: '
        Daca limitele lungimii numelui unui produs e intre 1 si 50 caractere
        Daca nu se incadreaza printati 'Nume Invalid - Lungimea numelui trebuie sa fie intre 1 si 50 de caractere'
    Introdu de la tastatura cu textul 'e-mail: '
    Generam ID-ul unic utilizatorului
    Generam data inregistrarii
    Citim din baza de date
    Generam structura dictionarului
    Scriem in baza de date
    """

    nume, email = "", ""
    while len(nume) < 1 or len(nume) > 50:
        nume = input("Introduceti numele utilizatorului de adaugat: \n")
        if len(nume) < 1 or len(nume) > 50:
            print("Nume Invalid, trebuie sa fie intre 1 si 50 caractere")
    while len(email) < 1:
        email = input("Introduceti email utilizator de adaugat: \n")
    id_utilizator = genereaza_id_utilizator(nume, email)
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
    datele_noastre = citeste_datele_din_baza_de_date()
    datele_noastre["utilizatori"][id_utilizator] = {
        "nume": nume,
        "email": email,
        "data_inregistrare": data_inregistrare.isoformat()
    }
    scrie_datele_in_baza_de_date(datele_noastre)


def listeaza_toti_utilizatorii():
    """
    Functia trebuie sa afiseze toti utilizatorii prezenti in baza de date.
    Afisarea ar trebui sa contina toate informatiile utilizatorilor
    """
    datele_noastre = citeste_datele_din_baza_de_date()
    utilizator = datele_noastre["utilizatori"]
    if utilizator:
        pprint(utilizator)
    else:
        print("Nu exista utilizatori.")


def sterge_un_utilizator():
    utilizator_de_sters = input("Introduceti ID-ul: \n")
    toate_datele = citeste_datele_din_baza_de_date()
    toate_datele["utilizatori"].pop(utilizator_de_sters)
    scrie_datele_in_baza_de_date(toate_datele)
