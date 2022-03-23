"""
6. 
Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)
"""

# Rezolvare:
# Ask the user for a number.
x = int(input("Enter a number higher than 0: "))
# Store the 2 given numbers into variables.
y = 5
z = 27
# Verify if the numbers are positive.
if x != 0 and x > 0:
	# Verify if the numbers are not in between the given range and print that.
	if not (x > y and x < z):
		print(f"{x} is not in bewtween {y} and {z}.")
	# If the numbers are not in the given range, print that they are not.	
	else:
		print(f"{x} is in between {y} and {z}.")	
# Inform the user that the numbers he typed are not positive.		
else:
	if x == 0:
		print("You must type a number higher than 0. Goodbye!")
	elif x < 0:
		print("You must type a positive number. Bye, bye!")			
