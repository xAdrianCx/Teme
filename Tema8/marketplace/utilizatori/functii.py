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
    Introdu de la tastatura cu textul 'e-: '
    Generam ID-ul unic utilizatorului
    Generam data inregistrarii
    Citim din baza de date
    Generam structura dictionarului
    Scriem in baza de date
    """
    nume, email = "", ""
    while True:
        nume = input("Introduceti numele utilizatorului: 'stop'-exit. \n")
        if nume == 'stop':
            print("La revedere!")
            email = 'stop'
            break
        elif len(nume) < 1 or len(nume) > 50:
            print("Lunigimea numelui trebuie sa fie intre 1 si 50 de caractere.")
        else:
            break
    while email != 'stop':
        email = input("Introduceti adresa de email: 'stop'-exit \n")
        if email == 'stop':
            print("La revedere!")
            break
        elif email != 'stop':
            for i in email:
                if "@" and ".com" not in email:
                    print("O adresa de email trebuie sa contina '@' si sa se termine in '.com'.")
                    break
                else:
                    baza_de_date = citeste_datele_din_baza_de_date()
                    id_utilizator = genereaza_id_utilizator(nume, email)
                    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0])).isoformat()
                    baza_de_date["utilizatori"][id_utilizator] = {
                        "nume": nume,
                        "email": email,
                        "data_inregistrare": data_inregistrare
                    }
                    scrie_datele_in_baza_de_date(baza_de_date)
        print(f"Utilizatorul {nume} a fost inregistrat cu succes.")
        break




def listeaza_toti_utilizatorii():
    """
    Functia trebuie sa afiseze toti utilizatorii prezenti in baza de date.
    Afisarea ar trebui sa contina toate informatiile utilizatorilor
    """
    baza_de_date = citeste_datele_din_baza_de_date()
    if len(baza_de_date['utilizatori']) > 0:
        print(f"Avem {len(baza_de_date['utilizatori'])} utilizatori inscrisi:")
        count = 0
        for i in baza_de_date["utilizatori"]:
            count += 1
            print(f"Utilizatorul nr. {count}: ")
            for j in baza_de_date["utilizatori"][i]:
                print("\t\t\t", j.title(), ":", "\t\t\t\t\t\t", baza_de_date["utilizatori"][i][j] )
            print("____________________________________________________________________________________________")


    else:
        print("Nu avem niciun utilizatori inscris.")

def sterge_un_utilizator():
    baza_de_date = citeste_datele_din_baza_de_date()
    while True:
        if baza_de_date["utilizatori"]:
            utilizator_de_sters = input("Introduceți identificatorul utilizatorului de sters: 'e'-exit\n")
            if utilizator_de_sters == 'e':
                print("La revedere!")
                break
            elif utilizator_de_sters.lower() not in baza_de_date["utilizatori"]:
                print(f"Nu am gasit utilizatorul cu id: {utilizator_de_sters}.")
            else:
                print(f"Utilizatorul cu ID {utilizator_de_sters} a fost sters.")
                baza_de_date["utilizatori"].pop(utilizator_de_sters)
                scrie_datele_in_baza_de_date(baza_de_date)
        else:
            print("Nu exista utilizatori de sters. O zi buna!")
            break