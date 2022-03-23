"""
7.
Avand lista
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterati prin ea
Afisati de cate ori apare 3
(nu aveti voie sa folositi count)
"""

# Rezolvare:
# Define the given list.
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Definde another list to keep track of how many times a number appears in our list.
duplicates = []
# Find how many times 3 appears in our list.
for i in range(len(numere)):
	if numere[i] == 3:
		duplicates.append(numere[i])
# Show how many times 3 appears in numere.
print(f"Number 3 appears {len(duplicates)} times in numere.")		


# List comprehension.
duplicates_2 = [numere[i] for i in range(len(numere)) if numere[i] == 3]
print(f"Number 3 appears {len(duplicates_2)} times in numere.")