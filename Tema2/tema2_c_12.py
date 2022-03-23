"""
12.Verifica daca x are exact 6 cifre
"""

# Rezolvare:
# Ask the user for a number.
x = int(input("Give me a number and i will tell you if it has exactly 6 digits." + 
	"\nType your number: "))	
# If user's number has exactrly six digits
# print that is has exactly six digits.														
if len(str(x)) == 6:																
	print(f"Number {x} has exactly six digits.")									
else:								
	# Print something in case user's number doesn't have exactly 6 digits.												
	print(f"Number {x} doesn't have exactly six digits.")							
	