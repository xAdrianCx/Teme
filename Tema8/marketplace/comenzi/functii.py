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
    # Define a dict to store the products.
    dict1 = {}
    # Define the variable to generate a unique id.
    detalii_comanda = []
    # set a flag.
    active = True
    # Define a num_lst to verify if the name of the product starts with a number(it can't start with a number).
    num_lst = []
    # Define a list to verify if the product is already in the list.
    product_keys = []
    print("Introduceti produsele din comanda. Pentru a termina, introduceti 'stop':\n")
    # Main loop.
    while active:
        # Get the name of the product.
        produs = input("Adaugati un nou produs la comanda. " +
                       "Numele trebuie sa contina mai mult de 2 litere: 'stop'-exit \n")
        # Iterate over the name of product to make sure it doesn't have any number in it.
        for i in produs:
            # If a number is found
            if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                # Append to num_lst.
                num_lst.append(i)
        if len(num_lst) > 0:
            print("Numele produsului nu poate contine numere. 'stop'-exit")
            num_lst = []
            # Product name can't be less than 2 letters.
        elif len(produs) < 2:
            print(f"Nu exista produsul {produs}.")
        elif produs.lower() == 'stop':
            break
        else:
            # Iterate over our list of dicts to find any duplicates.
            for i in detalii_comanda:
                for j in i.keys():
                    product_keys.append(j)
            # If duplicate is found.
            if produs.lower() in product_keys:
                while True:
                    global duplicate
                    duplicate = ""
                    if duplicate.lower() != 'da' or duplicate.lower() != 'nu':
                        duplicate = input(f"Aveti deja produsul {produs} in lista." +
                              " Doriti sa-i modificati cantitatea? 'da', 'nu' \n")
                    # If answer == no, we will add another product with the same name.
                    if duplicate == 'nu':
                        break
                    # Ask if we should modify it's quantity.
                    elif duplicate.lower() == 'da':
                        try:
                            cantitate = int(input(f"Introduceti noua cantitate pt. produsul {produs}: \n"))
                            for i in detalii_comanda:
                                for j in i.keys():
                                    if produs == j:
                                        # Del the existing key-value pair
                                        del i[j]
                                        # Add the modified key-value pair.
                                        detalii_comanda.append({produs: int(cantitate)})
                                    break
                                break
                            break
                        except ValueError:
                            print("Noua cantitate trebuie sa fie un nr. mai mare decat 0.")
            elif produs.lower() not in product_keys:
                try:
                    cantitate = input(f"Introduceti cantitatea dorita din produsul {produs}: 'stop'-exit\n")
                    if str(cantitate).lower() == 'stop':
                        active = False
                        break
                    elif int(cantitate) < 1:
                        print(f"Nu puteti comanda mai putin de 1. Incercati din nou. ")
                    else:
                        # Store the product and quantity into dict.
                        dict1[produs] = int(cantitate)
                        # Append the dict to the list.
                        detalii_comanda.append(dict1)
                        # Delete everything from dict1.
                        dict1 = {}
                except ValueError:
                    print("Trebuie sa introduceti un numar mai mare decat 0. Incercati din nou.")
    baza_de_date = citeste_datele_din_baza_de_date()
    id_comanda = genereaza_id_comanda(detalii_comanda)
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0])).isoformat()
    if len(detalii_comanda) > 0:
        baza_de_date["comenzi"][id_comanda] = {
            "id_comanda": id_comanda,
            "detalii_comanda": detalii_comanda,
            "data_inregistrare": data_inregistrare
        }
        print(f"Comanda cu id {id_comanda} a fost creata cu succes.")
    else:
        print("Nu s-a creat comanda pentru ca nu ati adaugat niciun produs.")
        pass
    scrie_datele_in_baza_de_date(baza_de_date)
    while True:
        answer = input("Doriti sa mai faceti o comanda?'da'-comanda noua, 'nu'-iesire \n")
        if answer.lower() == 'nu':
            print("La revedere!")
            break
        elif answer.lower() == 'da':
            inca_o_comanda()
            break
        else:
            print("Trebuie sa introduceti 'da' sau 'nu'.")


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
    while True:
        id_comanda = input("Introduceți identificatorul comenzii care se modifica: 'e'-exit\n")
        if id_comanda == 'e':
            print("La revedere!")
            active = False
            break
        elif id_comanda not in baza_de_date["comenzi"]:
            print(f"Comanda cu id-ul {id_comanda} nu a fost gasita. Reincercati.")
        else:
            break

    while active:
        actiune = input("Alegeti actiunea: " +
                            "('a' - adaugare produs; 'm' - modificare cantitate; 's'-sterge produs, 'e'-exit \n")
        if actiune == 'e':
            print("La revedere!")
            active = False
            break
        elif actiune == 'a':
            # Define a dict to store the new products.
            dict1 = {}
            # Define a list to store the name of products.
            prod_lst = []
            # Define a list to check if in the name of the product exists any number.
            num_lst = []
            while True:
                # Get the existing products in our order and store them into prod_lst.
                for i in baza_de_date['comenzi'][id_comanda]["detalii_comanda"]:
                    for j in i:
                        prod_lst.append(j)
                # Get the name of the product.
                produs = input("Adaugati un nou produs la comanda. " +
                               "Numele trebuie sa contina mai mult de 2 litere: 'e'-exit \n")
                # Iterate over the name of product to make sure it doesn't have any number in it.
                for i in produs:
                    # If a number is found
                    if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                        # Append to num_lst.
                        num_lst.append(i)
                if len(num_lst) > 0:
                    print("Numele produsului nu poate contine numere. 'stop'-exit")
                    num_lst = []
                    # Product name can't be less than 2 letters.
                elif produs.lower() == 'e':
                    print("La revedere!")
                    active = False
                    break
                elif len(produs) < 2:
                    print(f"Nu exista produsul {produs}.")
                    # Verify if produs is in the list already.
                elif produs in prod_lst:
                    print(f"Produsul {produs} exista deja." +
                          " Daca doriti sa-i modificati cantitatea," +
                          " mergeti pe ramura 'm' - modificare cantitate.")
                else:
                    while True:
                        try:
                            cantitate = input(f"Introduceti cantitatea dorita" +
                                              f" din produsul {produs}: 'e'-meniul anterior.\n")
                            if str(cantitate).lower() == 'e':
                                active = False
                                break
                            elif int(cantitate) < 1:
                                print(f"Nu puteti comanda mai putin de 1. Incercati din nou. ")
                            else:
                                # Store the product and quantity into dict.
                                dict1[produs] = int(cantitate)
                                # Append the dict to the list.
                                baza_de_date["comenzi"][id_comanda]["detalii_comanda"].append(dict1)
                                # Delete everything from dict1.
                                dict1 = {}
                                break
                        except ValueError:
                            print("Trebuie sa introduceti un numar mai mare decat 0. Incercati din nou.")

        elif actiune == 'm':
            num_lst = []
            prod_lst = []
            while True:
                # Get the existing products in our order and store them into prod_lst.
                if len(prod_lst) == 0:
                    for i in baza_de_date['comenzi'][id_comanda]["detalii_comanda"]:
                        for j in i:
                            prod_lst.append(j)
                # If products exists in list, keep them,
                # don't multiply them when passing through while loop.
                else:
                    prod_lst = prod_lst
                produs = input("Introduceti numele produsului caruia doriti sa-i modificati cantitatea: 'e'-exit \n")
                # Iterate over the name of product to make sure it doesn't have any number in it.
                for i in produs:
                    # If a number is found
                    if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                        # Append to num_lst.
                        num_lst.append(i)
                if len(num_lst) > 0:
                    print("Numele produsului nu poate contine numere. 'stop'-exit")
                    num_lst = []
                    # Product name can't be less than 2 letters.
                elif produs.lower() == 'e':
                    print("La revedere!")
                    active = False
                    break
                elif len(produs) < 2:
                    print(f"Nu exista produsul {produs}.")
                    # Verify if produs is in the list already.
                elif produs.lower() in prod_lst:
                    try:
                        cantitate = int(input(f"Introduceti noua cantitate pt. produsul {produs}: \n"))
                        # Iterate over the list "detalii_comanda" and get the dicts.
                        for i in baza_de_date["comenzi"][id_comanda]["detalii_comanda"]:
                            # Iterate over every dict in "detalii_comanda" to get the keys
                            for j in i:
                                # If a key is our product
                                if j == produs:
                                    # change the value of the product.
                                    i[j] = int(cantitate)
                    except ValueError:
                        print("Noua cantitate trebuie sa fie un nr. mai mare decat 0.")
                elif produs.lower() not in prod_lst:
                    print(f"Produsul {produs} nu este in lista de produse." +
                          " Pentru a-l adauga, mergeti pe ramura 'a' - adaugare produs.")
                    break
        elif actiune == 's':
            num_lst = []
            prod_lst = []
            while True:
                # Get the existing products in our order and store them into prod_lst.
                if len(prod_lst) == 0:
                    for i in baza_de_date['comenzi'][id_comanda]["detalii_comanda"]:
                        for j in i:
                            prod_lst.append(j)
                # If products exists in list, keep them,
                # don't multiply them when passing through while loop.
                else:
                    prod_lst = prod_lst
                produs = input("Introduceti numele produsului pe care doriti sa-l stergeti: 'e'-exit \n")
                # Iterate over the name of product to make sure it doesn't have any number in it.
                for i in produs:
                    # If a number is found
                    if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                        # Append to num_lst.
                        num_lst.append(i)
                if len(num_lst) > 0:
                    print("Numele produsului nu poate contine numere. 'stop'-exit")
                    num_lst = []
                    # Product name can't be less than 2 letters.
                elif produs.lower() == 'e':
                    print("La revedere!")
                    active = False
                    break
                elif len(produs) < 2:
                    print(f"Nu exista produsul {produs}.")
                elif produs.lower() in prod_lst:
                    index = ""
                    for i in range(len(baza_de_date["comenzi"][id_comanda]["detalii_comanda"])):
                        for j in baza_de_date["comenzi"][id_comanda]["detalii_comanda"][i].keys():
                            if j == produs:
                                index = i
                                # Delete the prduct.
                    index = int(index)
                    del baza_de_date["comenzi"][id_comanda]["detalii_comanda"][index]

                elif produs.lower() not in prod_lst:
                    print(f"Produsul {produs} nu este in lista de produse." +
                        " Pentru a-l adauga, mergeti pe ramura 'a' - adaugare produs.")
                    break
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
            print("________________________________________________________________________________________")
    else:
        print("Nu avem nicio comanda activa.")


def sterge_o_comanda():
    """
    Introdu de la tastatura cu textul  "Introduceți identificatorul comenzii de sters: "
    Cititi, stergeti, Scrieti

    """
    baza_de_date = citeste_datele_din_baza_de_date()
    while True:
        if baza_de_date["comenzi"]:
            comanda_de_sters = input("Introduceți identificatorul comenzii de sters: 'e'-exit\n")
            if comanda_de_sters == 'e':
                print("La revedere!")
                break
            elif comanda_de_sters.lower() not in baza_de_date["comenzi"]:
                print(f"Nu am gasit comanda cu id: {comanda_de_sters}.")
            else:
                print(f"Comanda cu ID {comanda_de_sters} a fost stearsa.")
                baza_de_date["comenzi"].pop(comanda_de_sters)
                scrie_datele_in_baza_de_date(baza_de_date)
        else:
            print("Nu exista comenzi de sters. O zi buna!")
            break
