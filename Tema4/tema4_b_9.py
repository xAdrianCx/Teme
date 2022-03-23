"""
9. 
Aceeasi lista
Iterati prin ea
Afisati cel mai mare numar
(nu aveti voie sa folositi max)
"""
# Rezolvare:
# Define the given list.
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Set a comparation variable.
highest = 0
# Iterate over a list and find the highest element in the list.
for i in numere:
	if i > highest:
		highest = i
print(f"Highest number in our list is {highest}.")		
