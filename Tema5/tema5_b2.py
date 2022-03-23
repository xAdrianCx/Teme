"""
2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
"""

# Rezolvare:
def odd_even(num):
	# Verify if a number is odd or even.
	if num % 2 == 0:
		return True
	else:
		return False

print(odd_even(11))		
print(odd_even(10))	