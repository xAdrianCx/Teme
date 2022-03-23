"""
12. Functie calculator care sa returneze 4 valori 
Suma, diferenta, inmultirea, impartirea a 2 numere

In final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
"""

# Rezolvare:
def calc(x, y):
	# A function which returns the sum, difference, product and quotient of two numbers.
	
	if y != 0:
		d = x / y
	else:
		d = "Can't divide by zero"	
	a = x + y
	b = x - y
	c = x * y
	return (f"Sum of {x} and {y}: {a}." + 
			f"\nDifference of {x} and {y}: {b}." + 
			f"\nProduct of {x} and {y}: {c}." + 
			f"\nQuotient of {x} and {y}: {d}.")
print(calc(10, 5))		
print(calc(-10, -5))	
print(calc(-10, 5))
print(calc(0, 10))
print(calc(10, 0))
