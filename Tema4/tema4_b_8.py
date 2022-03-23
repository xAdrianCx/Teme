"""
8. 
Aceeasi lista
Iterati prin ea
Calculati si afisati suma numerelor
(nu aveti voie sa folositi sum)
"""

# Rezolvare:
# Define the given list.
numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Define a variable to keep the result in.
result = 0
# Iterate over the list and calculate the sum of all elements.
for i in numbers:
	result += i
# Show the result.	
print(f"The sum of all elements in numbers is: {result}.")
	
