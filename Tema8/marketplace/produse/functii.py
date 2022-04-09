"""

Produsele ar trebui sa aiba structura:
("id_produs": {
    "nume_produs": "NumeleProdusului" - string,
    "pret": "Pret" - intreg/float,
    "data_inregistrare": "DataInregistrare" - string,
})

"""
import hashlib
from datetime import datetime
from baza_de_date.functii import citeste_datele_din_baza_de_date, scrie_datele_in_baza_de_date
from pytz import country_timezones, timezone


def genereaza_id_produs(nume_produs, pret):
    hash_object = hashlib.md5(bytes(nume_produs + pret, encoding='UTF-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def adauga_un_produs():
    '''
    Introdu de la tastatura cu textul 'Introduceti numele produsului de adaugat: '
        Daca limitele lungimii numelui unui produs e intre 1 si 50 caractere
        Daca nu se incadreaza printati 'Nume Invalid - Lungimea numelui trebuie sa fie intre 1 si 50 de caractere'
    Introdu de la tastatura cu textul 'Introduceti pretului produsului de adaugat: '
    Generam ID-ul unic produsului
    Generam data inregistrarii
    Citim din baza de date
    Generam structura dictionarului
    Scriem in baza de date
    '''
    # Set a flag.
    active = True
    # Define a num_lst to verify if the name of the product starts with a number(it can't start with a number).
    num_lst = []
    # Main loop.
    while active:
        # Get the name of the product.
        produs = input("Introduceti numele produsului de adaugat: 'stop'-exit \n")
        # Iterate over the name of product to make sure it doesn't have any number in it.
        for i in produs:
            # If a number is found
            if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                # Append to num_lst.
                num_lst.append(i)
        if len(num_lst) > 0:
            print("Numele produsului nu poate contine numere.")
            num_lst = []
            # Length of product's name can't be less than 1 letter or larger than 50.
        elif len(produs) < 1 or len(produs) > 50:
            print(f"Numele produsului trebuie sa fie intre 1 si 50 de caractere.")
        # Quit if 'stop' is entered.
        elif produs == 'stop':
            print("La revedere!")
            break
        else:
            try:
                pret = input(f"Introduceti pretul produsului {produs}: 'stop'-exit\n")
                if str(pret).lower() == 'stop':
                    print("La revedere!")
                    active = False
                    break
                elif float(pret) < 0.00:
                    print(f"Un produs nu poate avea pretul mai mic decat 0.00. Incercati din nou. ")
            except ValueError:
                print("Trebuie sa introduceti un numar mai mare decat 0. Incercati din nou.")
            else:
                # Read from database.
                baza_de_date = citeste_datele_din_baza_de_date()
                # Generate the id of product.
                id_produs = genereaza_id_produs(produs, pret)
                # verify if there are products in our database.
                if baza_de_date["produse"]:
                    # Store all products from database in a list.
                    lst_prod = []
                    for i in list(baza_de_date["produse"]):
                        for j in list(baza_de_date["produse"][i]):
                            if baza_de_date["produse"][i][j] == produs:
                                lst_prod.append(baza_de_date["produse"][i][j])
                    # If the product exists, can't be added a second time with exactly the same name.
                    if produs in lst_prod:
                        print(f"Produsul {produs} exista deja.")
                    # If the product doesn't exist in database, add it.
                    else:
                        baza_de_date["produse"][id_produs] = {
                            "nume produs": produs,
                            "pret": float(pret),
                            "data inregistrare": datetime.now(
                                tz=timezone(country_timezones.get("RO")[0])).isoformat(),
                        }
                        scrie_datele_in_baza_de_date(baza_de_date)
                        print(f"S-a adaugat produsul {produs} la pretul de {pret}.")
                # If our database is empty, add the product directly.
                else:
                    baza_de_date["produse"][id_produs] = {
                        "nume produs": produs,
                        "pret": float(pret),
                        "data inregistrare": datetime.now(tz=timezone(country_timezones.get("RO")[0])).isoformat(),
                    }
                    # Write to database.
                    scrie_datele_in_baza_de_date(baza_de_date)


def listeaza_toate_produsele():
    """
    Functia trebuie sa afiseze toate produsele prezente in baza de date.
    Afisarea ar trebui sa contina toate informatiile produselor
    """
    baza_de_date = citeste_datele_din_baza_de_date()
    count = 0
    print(f"Avem {len(baza_de_date['produse'])} produse inscrise deja.")
    for i in baza_de_date['produse']:
        count += 1
        print(f"Produsul nr. {count} --> ID Produs: {i}")
        for j in baza_de_date['produse'][i]:
            print("\t\t\t\t  ", j.title(), ":", "\t\t\t", baza_de_date["produse"][i][j])
        print("___________________________________________________________________________________________")

def sterge_produs():
    baza_de_date = citeste_datele_din_baza_de_date()
    while True:
        if baza_de_date["produse"]:
            produs_de_sters = input("Introduceți identificatorul produsului de sters: 'e'-exit\n")
            if produs_de_sters == 'e':
                print("La revedere!")
                break
            elif produs_de_sters.lower() not in baza_de_date["produse"]:
                print(f"Nu am gasit produsul cu id: {produs_de_sters}.")
            else:
                print(f"Produsul cu ID {produs_de_sters} a fost sters.")
                baza_de_date["produse"].pop(produs_de_sters)
                scrie_datele_in_baza_de_date(baza_de_date)
        else:
            print("Nu exista produse de sters. O zi buna!")
            break
