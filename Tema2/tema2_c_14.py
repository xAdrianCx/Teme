"""
14. x, y, z (int)
Afiseaza care este cel mai mare dintre ele?
"""

# Rezolvare: 
# Ask the user for 3 numbers.
x = int(input("Give me three numbers and i will tell you which one is the greatest." + 
	"\nType the 1st number: "))															
y = int(input("Type the 2nd number: "))														
z = int(input("Type the 3rd number: "))
# If x is the greatest, print x.
if x >= y and x >= z:										
	print(f"Number {x} is the greatest number.")											
elif y >= x and y >= z:								
	# If y is the greatest, print y.	
	print(f"Number {y} is the greatest number.")													
elif z >= x and z >= y:								
	# If z is the greatest, print z.		
	print(f"Number {z} is the greatest number.")												


# (Altfel de) Rezolvare:
# Ask the user for 3 numbers.
x = int(input("Give me three numbers and i will tell you which one is the greatest." + 
	"\nType the 1st number: "))															
y = int(input("Type the 2nd number: "))														
z = int(input("Type the 3rd number: "))
# Print the greatest number.
print(f"The greatest number from {x}, {y} and {z} is " + str(max(x, y, z)) + ".")   
