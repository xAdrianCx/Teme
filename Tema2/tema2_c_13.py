"""
13.
Verifica daca x este numar par sau impar
"""

# Rezolvare:
# Ask the user for a number.
x = int(input("Enter a number and i will tell you if it's even or odd." + 
	"\nType your number: "))
# If x modulo == 0 it has to be an even number.													
if x % 2 == 0:	
	# Print that the number is even.															
	print(f"Number {x} is an even number.")	
# If it passes the if statement, it has be be odd.								
else:									
	# Print that the number is odd.									
	print(f"Number {x} is an odd number")										
	