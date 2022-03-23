"""
9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
Primul numar x este mai mare decat al doilea nr y
Al doilea nr y este mai mare decat primul nr x
Numerele sunt egale. 
"""

# Rezolvare:
def check_numbers(first, second):
	# Print if 2 numbers are equal or if a number is higher than the other.
	if first > second:
		print(f"First number: {first} is higher than the 2nd number: {second}.")
	elif second > first:
		print(f"Second number: {second} is higher than the 1st number: {first}.")	
	else:
		print(f"The two numbers are equal.")	
check_numbers(10, 5)
check_numbers(1, 2)
check_numbers(5, 5)
