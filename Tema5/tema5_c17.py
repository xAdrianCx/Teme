"""
17. Functie care primesete 2 liste de numere (numerele pot fi dublate)
Returnati numerele comune 

Ex:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Raspuns: {2, 3}
"""

# Rezolvare:
def common(a, b):
	# A function that receives 2 lists and returns only the common elements in the lists.
	return set(a).intersection(b)
print(common([1, 1, 2, 3], [2, 2, 3, 4]))	