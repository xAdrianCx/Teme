"""
6. 
Avand dict
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
Vine un client cu un buget de 15000 euro
Prezentati doar masinile care se incadreaza in acest buget
Iterati prin dict.items() si accesati masina si pretul
Printati Pentru un buget de sub 15000 euro puteti alege masina xLastun
Iterati prin lista
"""

# Rezolvare:
# Definde the given dict.
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
# Iterate over the keys and values in a dict and show only the keys with a value lower than 15000.
for item, value in pret_masini.items():
	if value < 15000:
		print(f"For a price range of 15000 you can pick {item} for a price of {value}.")