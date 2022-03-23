"""
10.
Aceeasi lista
Iterati prin ea
Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
Ex: daca e 3, sa devina -3
Afisati noua lista
"""


# Rezolvare:
# Define the given list.
numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterate over a list and turn all positive numbers into negative numbers.
for i in range(len(numbers)):
	if numbers[i] > 0:
		numbers[i] *= (-1)	
print(numbers)


# (Altfel de) Rezolvare:
# Define the given list.
numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterate over a list and turn all positive numbers into negative numbers.
for i in range(len(numbers)):
	if numbers[i] > 0:
		numbers[i] = "-" + str(numbers[i])
for i in range(len(numbers)):
	numbers[i] = int(numbers[i])		

print(numbers)


