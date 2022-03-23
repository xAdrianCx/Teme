"""
5. 
Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
"""

# Rezolvare:
# Ask for 2 numbers.
x = int(input("Enter two numbers and i will show you the difference between them: " +
	"\nEnter the 1st number: "))																				
y = int(input("Enter the 2nd number: "))
# Substract the 2nd number from the 1st to verify the difference.
# Make sure 1st number is not equal to 2nd number.
if x > y:	
	# Verify the difference between the numbers.		
	if (x - y) < 5:
		print(f"The difference between {x} and {y} is {x - y}.")
	# We don't have to show the result if it is higher than 5,
	# but we inform the user that it's higher than 5.	
	elif (x - y) > 5:
		print(f"The difference between {x} and {y} is bigger than 5.")	
elif y > x:
	# Verify the difference between the numbers.	
	if (y - x) < 5:
		print(f"The difference between {y} and {x} is {y - x}.")
	# We don't have to show the result if it is higher than 5,
	# but we inform the user that it's higher than 5.	
	elif (y - x) > 5:
		print(f"The difference between {x} and {y} is bigger than 5.")		
# Say something if the numbers are equal.
else:
	print("The two numbers are equal. There's no difference between them.")
