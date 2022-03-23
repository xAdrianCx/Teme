"""
9. 
Printati cei 3 elevi si notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o veti lua folosindu-va de cheie
"""

# Rezolvare:
# Define a dictionary.
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Show what grades the 3 students got.
print(f"Ana got an {dict1.get('Ana')} today.")
print(f"Gigel got a {dict1.get('Gigel')} today.")
print(f"Dorel got a {dict1.get('Dorel')} today.")


# (Altfel de) Rezolvare:
# (we're gonna use the same dict.)
# Define a variable to store the students's names(dict keys).
list_keys = list(dict1.keys())
# Show the grades the students got today.
print(f"{list_keys[0]} got an {dict1.get(list_keys[0])} today.")
print(f"{list_keys[1]} got a {dict1.get(list_keys[1])} today.")
print(f"{list_keys[2]} got a {dict1.get(list_keys[2])} today.")
