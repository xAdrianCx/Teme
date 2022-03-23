"""
10.
Dorel a facut contestatie si a primit 6
Modificati nota lui Dorel in 6
Printati nota dupa modificare
"""

# Rezolvare:
# Define a dictionary.
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Modifying Dorel's grade using dict key.
dict1["Dorel"] = 6
# Show the result.
print(f"Dorel's grade after modification is: {dict1['Dorel']}.")
# Modifying Dorel's grade using update() function.
dict1.update({"Dorel": 6})
# Show the result.
print(f"Dorel's grade after second modification is: {dict1['Dorel']}.")
