"""
Comenzile ar trebui sa aiba structura:
("id_comanda": {
    "id_comanda": "Idcomanda" - string,
    "detalii_comanda":
        [{"IdProdus": CantitateProdus}]
        - lista de dictionare de forma IdProdus (string): CantitateProdus (numar intreg),
    "data_inregistrare": "DataInregistrare" - string,
})

"""
import hashlib
import json
from datetime import datetime
from baza_de_date.functii import citeste_datele_din_baza_de_date, scrie_datele_in_baza_de_date
from pytz import country_timezones, timezone


def genereaza_id_comanda(detalii_comanda):
    hash_object = hashlib.md5(bytes(json.dumps(detalii_comanda), encoding='UTF-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def adauga_o_comanda():
    """
    Introdu de la tastatura cu textul: "Introduceti produsele din comanda. Pentru a termina, introduceti 'stop':\n"
    Ca prim input dam Produsul, apoi Cantitatea
    Generam ID-ul unic comenzii
    Generam data inregistrarii
    Citim din baza de date
    Generam structura dictionarului
    Scriem in baza de date
    """

    # Define an empty dict to store the inputs.
    dict1 = {}
    # Define the variable we need to geneerate an order ID.
    detalii_comanda = []
    # Main loop.
    global active
    active = True
    while active:
        print("Introduceti produsele din comanda. Pentru a termina, introduceti 'stop'.")
        produs = input("Introduceti produsul: \n")
        if len(produs) < 2:
            print(f"Nu exista produsul {produs}")
        elif produs.lower() == "stop":
            active = False
            break
        else:
            try:
                cantitate = int(input(f"Introduceti cantitatea dorita din produsul {produs}: \n"))
                if int(cantitate) < 1:
                    print(f"Nu puteti comanda {cantitate} din {produs}.")
                elif str(cantitate).lower() == "stop":
                    active = False
                    break
                else:
                    # Store the product and quantity into dict.
                    dict1[produs] = cantitate
                    # Append the dict to the list.
                    detalii_comanda.append(dict1)
                    # Delete everything from dict1.
                    dict1 = {}
            except ValueError:
                print("Trebuie sa introduceti un numar.")
    baza_de_date = citeste_datele_din_baza_de_date()
    # Generate the Order ID.
    id_comanda = genereaza_id_comanda(detalii_comanda)
    # Set the database style.
    baza_de_date["comenzi"][id_comanda] = {
        "id_comanda": id_comanda,
        "detalii_comanda": detalii_comanda,
        "data_inregistrare": datetime.now(tz=timezone(country_timezones.get("RO")[0])).isoformat()
    }
    # Get rid of empty order.
    # Getting rid of empty list in "comenzi"[id_comanda].
    if len(baza_de_date["comenzi"][id_comanda]["detalii_comanda"]) == 0:
        comanda_de_sters = id_comanda
        baza_de_date["comenzi"].pop(comanda_de_sters)
        scrie_datele_in_baza_de_date(baza_de_date)
    # Write everything to database.
    scrie_datele_in_baza_de_date(baza_de_date)
    active = False
    print("Comanda a fost creata cu succes.")
    active = False
    answer = ""
    while True:
        answer = input("Doriti sa mai faceti o comanda?'da'-comanda noua, 'stop'-iesire \n")
        if answer.lower() == 'da':
            active = True
            inca_o_comanda()
        elif answer.lower() == 'stop':
            print("La revedere!")
            break
        else:
            print("Trebuie sa introduceti 'da' sau 'stop'.")

def inca_o_comanda():
    adauga_o_comanda()


def modifica_comanda():
    """
    Introduceti de la tastatura textul: "Introduceți identificatorul comenzii care se modifica: "
    Creeam o logica care sa primeasca ca input de la tastatura 4 variante de actiune:
        "Alegeti actiunea ('a' - adaugare produs; 'm ' - modificare cantitate; 's'-sterge produs, 'e'-exit \n")
        Creeam logica pentru cele 4 variante
        Ca input trebuie sa dam produsul si cantitatea pentru 'a' si 'm', pentru 's' dam identificatorul
        Din nou, Citim, Actionam, Scriem
    """

    baza_de_date = citeste_datele_din_baza_de_date()
    active = True
    id_comanda = input("Introduceți identificatorul comenzii care se modifica: \n")
    while active:
        if id_comanda.lower() == "e":
            print("La revedere!")
            active = False
            break
        elif id_comanda not in baza_de_date["comenzi"]:
            id_comanda = input("ID-ul comenzii nu a fost gasit. Incercati din nou. 'e'-exit \n")
        else:
            actiune = ""
            while actiune.lower() != "a" or actiune.lower() != "m" or actiune.lower() != "s" or actiune.lower() != "e":
                actiune = input("Alegeti actiunea" +
                      "\n ('a' - adaugare produs; 'm ' - modificare cantitate; 's'-sterge produs, 'e'-exit) \n")
                if actiune.lower() == "e":
                    print("La revedere!")
                    active = False
                    break
                elif actiune.lower() == "a":
                    dict1 = {}
                    produs = ""
                    while len(produs) < 2:
                        produs = input("Introduceti numele produsului pe care doriti sa-l adaugati: \n")
                        if produs.lower() == "e":
                            print("Meniul anterior.")
                            active = False
                            break
                        elif len(produs) < 2:
                            print(f"Nu exista produsul {produs}")
                        else:
                            try:
                                cantitate = int(input(f"Introduceti cantitatea dorita din produsul {produs}: \n"))
                                if str(cantitate).lower() == "e":
                                    print("Meniul anterior.")
                                    active = False
                                    break
                                elif int(cantitate) < 1:
                                    print(f"Nu puteti comanda {cantitate} din {produs}.")
                            except ValueError:
                                print("Trebuie sa introduceti un numar.")
                            else:
                                # Store the product and quantity into dict.
                                dict1[produs] = cantitate
                                # Read from database.
                                baza_de_date = citeste_datele_din_baza_de_date()
                                # If product already exists.
                                lst_dict11 = list(dict1.keys())
                                lst_keys = []
                                for i in baza_de_date["comenzi"][id_comanda]["detalii_comanda"]:
                                    for j in i.keys():
                                        lst_keys.append(j)
                                for i in baza_de_date["comenzi"][id_comanda]["detalii_comanda"]:
                                    for j in lst_dict11:
                                        if j not in lst_keys:
                                            # Add item to the order.
                                            baza_de_date["comenzi"][id_comanda]["detalii_comanda"].append({j: dict1[j]})
                                            scrie_datele_in_baza_de_date(baza_de_date)
                                            break
                                        else:
                                            # Update the values.
                                            print(f"Produsul {j} exista deja, daca doriti sa-l modificati, mergeti" +
                                                " pe ramura modificare cantitate.")
                                        break
                                    break
                                dict1 = {}
                elif actiune.lower() == "m":
                    while active:
                        baza_de_date = citeste_datele_din_baza_de_date()
                        produs = input("Introduceti numele produsului a carui cantitate doriti sa o modificati: 'e'-exit \n")
                        dict_keys = []
                        for i in baza_de_date["comenzi"][id_comanda]["detalii_comanda"]:
                            for j in i.keys():
                                dict_keys.append(j)
                        if produs.lower() == "e":
                            print("Meniul anterior.")
                            active = False
                            break
                        elif produs not in dict_keys:
                            print(f"Nu exista produsul {produs}.")
                        else:
                            try:
                                cantitate = int(input(f"Introduceti cantitatea pt. produsul {produs}:  \n"))
                                if str(cantitate).lower() == "e":
                                    print("Meniul anterior.")
                                    active = False
                                    break
                                elif int(cantitate) < 1:
                                    # If quantity is modified to 0, delete the product.
                                    print(f"Daca doriti cantitate 0, stergeti produsul {produs} din macheta 'sterge produs'.")
                            except ValueError:
                                print("Trebuie sa introduceti un numar.")
                            else:
                                # Store the product and quantity into dict.
                                dict1 = {}
                                dict1[produs] = cantitate
                                for i in range(len(baza_de_date["comenzi"][id_comanda]["detalii_comanda"])):
                                    for j in baza_de_date["comenzi"][id_comanda]["detalii_comanda"][i].keys():
                                        if j == produs:
                                            # Modify the product's quantity.
                                            baza_de_date["comenzi"][id_comanda]["detalii_comanda"][i][j] = cantitate
                                            scrie_datele_in_baza_de_date(baza_de_date)
                                        break
                                    break
                elif actiune.lower() == "s":
                    while active:
                        produs = input(
                            "Introduceti numele produsului a carui cantitate doriti sa o modificati: 'e'-exit \n")
                        dict_keys = []
                        for i in baza_de_date["comenzi"][id_comanda]["detalii_comanda"]:
                            for j in i.keys():
                                dict_keys.append(j)
                        if produs.lower() == "e":
                            print("Meniul anterior.")
                            active = False
                            break
                        elif produs not in dict_keys:
                            print(f"Nu exista produsul {produs}.")
                        else:
                            for i in range(len(baza_de_date["comenzi"][id_comanda]["detalii_comanda"])):
                                for j in baza_de_date["comenzi"][id_comanda]["detalii_comanda"][i].keys():
                                    if j == produs:
                                        # Delete the prduct.
                                        baza_de_date["comenzi"][id_comanda]["detalii_comanda"][i].pop(j)
                                        scrie_datele_in_baza_de_date(baza_de_date)
                                    break
                                break

    # Getting rid of empty dicts in "detalii_comanda".
    baza_de_date["comenzi"][id_comanda] = {"detalii_comanda": [i for i in baza_de_date["comenzi"][id_comanda]["detalii_comanda"] if i]}
    scrie_datele_in_baza_de_date(baza_de_date)

def listeaza_toate_comenzile():
    """
    Functia trebuie sa afiseze toate comenzile prezente in baza de date.
    Afisarea ar trebui sa contina toate informatiile comenzilor
    """
    baza_de_date = citeste_datele_din_baza_de_date()
    if len(baza_de_date['comenzi']) > 0:
        print(f"Avem {len(baza_de_date['comenzi'])} comenzi active:")
        count = 0
        for i in baza_de_date["comenzi"]:
            count += 1
            print(f"Comanda nr. {count}: ")
            for j in baza_de_date["comenzi"][i]:
                print("\t\t\t", j.title(), ":", "\t\t\t", baza_de_date["comenzi"][i][j])
    else:
        print("Nu avem nicio comanda activa.")

def sterge_o_comanda():
    """
    Introdu de la tastatura cu textul  "Introduceți identificatorul comenzii de sters: "
    Cititi, stergeti, Scrieti

    """
    baza_de_date = citeste_datele_din_baza_de_date()
    comanda_de_sters = ""
    while comanda_de_sters.lower() != "nu":
        comanda_de_sters = input("Introduceți identificatorul comenzii de sters: 'e'-exit\n")
        if comanda_de_sters.lower() != 'e' and comanda_de_sters not in baza_de_date["comenzi"]:
            print(f"Nu am gasit comanda cu id: {comanda_de_sters}.")
        elif comanda_de_sters.lower() == 'e':
            print("La revedere!")
            break
        else:
            baza_de_date["comenzi"].pop(comanda_de_sters)
            scrie_datele_in_baza_de_date(baza_de_date)
