"""
15. Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
Ex: daca dam nr 3
Suma va fi 6 (0+1+2+3)
"""

# Rezolvare:
def additon(num):
	# A function that receives a number and calculates the sum of all numbers 'til that number.
	# Set a count flag.
	count = 0
	# Iterate over the entire range and add the new value of i to the last one.
	if num >= 0:
		for i in range(num + 1):
			count += i
		return count
	elif num < 0:
		for i in range(num, 0):
			count += i
		return count	
print(additon(11))	
print(additon(45))	
print(additon(-34))
print(additon(-11))


# (Altfel de) Rezolvare:
def sum_range(number):
	if number >= 0:
		return sum(range(number + 1))
	elif number < 0:
		return sum(range(number, 0))
print(sum_range(11))
print(sum_range(45))
print(sum_range(-34))
print(sum_range(-11))