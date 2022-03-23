"""
11.
Gigel se transfera din clasa
Cautati o functie care sa il stearga
Vine un coleg nou. Adaugati Ionica, cu nota 9
Printati dictionarul schimbat
"""

# Rezolvare:
# Define a dictionary.
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Remove Gigel from the classroom.
dict1.pop('Gigel')
# Show that Gigel has left the classroom.
print(dict1)
# Ionica is comming to the classroom.
dict1.update({"Ionica": 9})
# Show that Ionica has been added to the classroom.
print(dict1)
