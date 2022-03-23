"""
8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
"""

# Rezolvare:
def positive_numbers(randoms):
	# Return a list of only positive numbers from a given list.
	positives = []
	for i in randoms:
		if i > 0:
			positives.append(i)
	return positives		
print(positive_numbers([0, 1, 4, 5, 7, -12, 53, 76, -98, 111, -10, 9, 99, -12, 13, 35, 66]))	
print(positive_numbers([33, -44, 55, -66, 77, 88, -99, 11, 22]))	
