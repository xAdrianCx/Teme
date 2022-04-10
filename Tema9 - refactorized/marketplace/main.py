
from common.utils import adaugare, modifica_comanda, listare, stergere

if __name__ == '__main__':
    def mesaj_de_iesire():
        print("O zi frumoasa in continuare")

    maparea_comenzilor_la_functii = {
        "adaugare": adaugare,
        "modifica_comanda": modifica_comanda,
        "listare": listare,
        "stergere": stergere,
        "exit": mesaj_de_iesire
    }
    actiune = None
    while actiune != "exit":
        actiune = input("Introdu o comanda:\n")
        functia_de_executie = maparea_comenzilor_la_functii.get(actiune)
        if functia_de_executie is None:
            print("Actiune Invalida")
            print(f"Actiuni Valide: {','.join(maparea_comenzilor_la_functii.keys())}")
        else:
            functia_de_executie()
