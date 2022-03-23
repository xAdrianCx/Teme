"""
c. Optionale (may need google)

11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Iterati prin lista alte_numere 
Populati corect celelalte liste
Afisati cele 4 liste la final
"""

# Rezolvare:
# Define the given lists.
other_numbers = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
even_numbers = []
odd_numbers = []
positive_numbers = []
negative_numbers = []
# Iterate over the list alte_numere.
for i in other_numbers:
	if i % 2 == 0:							# Verify if the nubers are even.
		even_numbers.append(i)
	if i % 2 != 0:							# Verify if the numbers are odd.
		odd_numbers.append(i)
	if i > 0:								# Verify for positive numbers.
		positive_numbers.append(i)
	if i < 0:								# Verify for negative numbers.
		negative_numbers.append(i)
# Show the lists.
print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
print(f"Positive numbers: {positive_numbers}")
print(f"Negative numbers: {negative_numbers}")						