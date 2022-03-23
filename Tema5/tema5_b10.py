"""
0. Functie care primeste un numar si un set de numere.
Printeaza ‘am adaugat numarul nou in set’ + returneaza True
Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
"""

# Rezolvare:
def check_num_in_set(x, y):
	# Verify if a number is in a given set and if it's not, add it into the set and then return True
	# if it is in the set, don't do anything, just return False.
	if x not in y:
		print(f"I've added the new number to the set.")
		return True
	elif x in y:
		print(f"I didn't add the new number to the set. It's already into the set.")
		return False
# Using the print function.		
print(check_num_in_set(3, {10, 4, 5, 7, 88, 99, 34,2}))
print(check_num_in_set(4, {3, 5, 7, 4, 8, 2, 2, 3, 4, 6}))		
# Checking the result without the print function.
check_num_in_set(3, {10, 4, 5, 7, 88, 99, 34,2})
check_num_in_set(4, {3, 5, 7, 4, 8, 2, 2, 3, 4, 6})
