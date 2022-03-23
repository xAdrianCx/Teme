"""
3.
Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
"""

# Rezolvare:
# Ask for a number.
number = int(input("Enter a number and i will tell you if it's positive, negative or neutral(0): "))
# Verify if the number is 0, positive or negative.
if number == 0:
	print(f"{number} is neighter positive nor negative, it's neutral.")
elif number > 0:
	print(f"{number} is a positive number.")
else:
	print(f"{number} is a negative number")
