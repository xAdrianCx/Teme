"""
11.Verifica daca x are minim 4 cifre
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
"""

# Rezolvare:
# Ask the user for a number.
x = int(input("Type a number and i will tell you if it has more than 4 digits. " + 
	"\nType your number: "))
# If user's number has 4 or more digits
# print that is has 4 or more digits.															
if len(str(x)) >= 4:																
	print(f"Number {x} has 4 or more digits.")		
# Else If user's number doesn't even have 4 digits(has less than 4 digits)
# print that it doesn't even have 4 digits.											
elif not len(str(x)) >= 4:																
	print(f"Number {x} doesn't even have 4 digits.")											
	