"""
7.
x si y (int)
Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
"""

# Rezolvare:
# Ask the user for 2 numbers.
x = int(input("Give me 2 numbers and i will tell you " + 
	"\nwhich is higher or if they are equal." +				
	"\nEnter the 1st number: "))
y = int(input("Enter the 2nd number: "))

if x == y:
	# Inform the user that the numbers are equal.
	print("The 2 numbers you typed are equal.")    			
elif x > y:
	# Inform the user which number is higher.
	print(f"{x} is higher than {y}.")  			 			
elif x < y:
	# Inform the user which number is higher.
	print(f"{y} is higher than {x}.")			 			


# (Altfel de) Rezolvare:
# Ask the user for 2 numbers.
x = int(input("Give me 2 numbers and i will tell you " +  
	"\nwhich is higher or if they are equal." +  			
	"\nEnter the 1st number: "))
y = int(input("Enter the 2nd number: "))
if x != y:
	# Inform the user which number is higher.
	print(f"{max(x, y)} is higher than {min(x, y)}.")		
else:
	# Inform the user that the numbers are equal.
	print("The numbers you typed are equal.")   				
