"""
1.
Declara o lista note_muzicale in care sa pui do re mi etc pana la do
Afiseaz-o
Inverseaza ordinea folosind slicing si suprascrie aceasta lista
Printeaza varianta actuala (inversata)
Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, 
adica sa ii inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, 
deoarece metoda face asta automat)
Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala

Concluzii: slicing e temporar, daca vrei sa pastrezi noua varianta va trebuie 
sa suprascrii lista sau sa o salvezi intr-o lista noua. Metoda gasita de tine, 
face suprascrierea automat si permanentizeaza aceste modificari. 
Ambele variante isi gasesc utilitatea in functie de ce ne dorim in acel moment. 
"""

# Rezolvare:
# Define a list with musical notes.
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
# Using slicing, store the reversed list in a new one.
reversed_note_muzicale = note_muzicale[::-1]
# Show the new(reversed) list.
print(f"Reversed list: {reversed_note_muzicale}")
# Now use the reversed method to reverse the list again.
reversed_note_muzicale.reverse()
# Show the list.
print(f"Reversed reversed list: {reversed_note_muzicale}")
