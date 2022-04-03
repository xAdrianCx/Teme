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
    hash_object = hashlib.md5(bytes(nume_produs + str(pret), encoding='UTF-8'))
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


    nume_produs = ""
    while True:
        nume_produs = input(("Introduceti numele produsului: 'e'-exit\n"))
        if len(nume_produs) < 1 or nume_produs == "" or len(nume_produs) > 50:
            print("Nume invalid. Trebuie sa fie intre 1 si 50 caractere.")
        elif nume_produs == 'e':
            print("La revedere!")
            break
        else:
            try:
                pret_produs = float(input(f"Introduceti pretul pt. {nume_produs}: \n"))
                if float(pret_produs) < 0:
                    print(f"Produsul nu poate avea pretul {pret_produs}.")
            except ValueError:
                print("Trebuie sa introduceti un numar.")
            else:
                baza_de_date = citeste_datele_din_baza_de_date()
                id_produs = genereaza_id_produs(nume_produs, pret_produs)
                if baza_de_date["produse"]:
                    lst_prod = []
                    for i in list(baza_de_date["produse"]):
                        for j in  list(baza_de_date["produse"][i]):
                            if baza_de_date["produse"][i][j] == nume_produs:
                                lst_prod.append(baza_de_date["produse"][i][j])
                    if nume_produs in lst_prod:
                        print(f"{nume_produs.title()} exista deja.")
                    else:
                        baza_de_date["produse"][id_produs] = {
                            "nume produs": nume_produs,
                            "pret": pret_produs,
                            "data inregistrare": datetime.now(tz=timezone(country_timezones.get("RO")[0])).isoformat(),
                        }
                        scrie_datele_in_baza_de_date(baza_de_date)
                else:
                    baza_de_date["produse"][id_produs] = {
                        "nume produs": nume_produs,
                        "pret": pret_produs,
                        "data inregistrare": datetime.now(tz=timezone(country_timezones.get("RO")[0])).isoformat(),
                    }
                    scrie_datele_in_baza_de_date(baza_de_date)

def listeaza_toate_produsele():
    """
    Functia trebuie sa afiseze toate produsele prezente in baza de date.
    Afisarea ar trebui sa contina toate informatiile produselor
    """
    baza_de_date = citeste_datele_din_baza_de_date()
    count = 0
    print(f"Avem {len(baza_de_date['produse'])} produse in inscrise deja.")
    for i in baza_de_date['produse']:
        count += 1
        print(f"Comanda nr. {count} --> ID Comanda: {i}")
        for j in baza_de_date['produse'][i]:
            print("\t\t\t", j.title(), ":", "\t\t\t", baza_de_date["produse"][i][j])


def sterge_produs():
    while True:
        baza_de_date = citeste_datele_din_baza_de_date()
        if not baza_de_date['produse']:
            print("Nu ati adaugat niciun produs inca. Adaugati produse intai.")
            break
        else:
            produs_de_sters = input("Introduceti ID-ul produsului pe care doriti sa-l stergeti: 'e'-exit \n")
            if produs_de_sters == "e":
                print("La revedere!")
                break
            else:
                if produs_de_sters in baza_de_date['produse']:
                    del baza_de_date["produse"][produs_de_sters]
                    scrie_datele_in_baza_de_date(baza_de_date)






