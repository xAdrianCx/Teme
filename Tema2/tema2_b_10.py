"""
10.
Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
"""

# Rezolvare:
# Store the USA grades into variables.
USA_A = "A"
USA_B = "B"
USA_C = "C"
USA_D = "D"
USA_E = "E"
USA_F = "F"
# Store Romanian grades into variables.
RO_4 = 4
RO_6 = 6
RO_7 = 7
RO_8 = 8
RO_9 = 9

# Get a grade from the user.
grade = float(input("What grade did u get today: "))
# Make sure the user inserts a number between 1 and 10.	
if grade >= 1.0 and grade <= 10.0:
	# Verify if the grade is smaller or equal to 4.		
	if grade <= RO_4:
		# Print the result and compare it to the USA.													
		print(f"U've got {grade}. In USA you would've gotten {USA_F}.")	
	# Verify if the grade is smaller or equal to 6.	
	elif grade > RO_4 and grade <= RO_6:
		# Print the result and compare it to the USA.																
		print(f"U've got {grade}. In USA you would've gotten {USA_E}.")	
	# Verify if the grade is smaller or equal to 7.	
	elif grade > RO_6 and grade <= RO_7:	
		# Print the result and compare it to the USA.								
		print(f"U've got {grade}. In USA you would've gotten {USA_D}.")	
	# Verify if the grade is smaller or equal to 8.	
	elif grade > RO_7 and grade <= RO_8:								
		# Print the result and compare it to the USA.	
		print(f"U've got {grade}. In USA you would've gotten {USA_C}.")	
	# Verify if the grade is smaller or equal to 9.	
	elif grade > RO_8 and grade <= RO_9:
		# Print the result and compare it to the USA.									
		print(f"U've got {grade}. In USA you would've gotten {USA_B}.")	
	# Verify if the grade is greater then 9.		
	elif grade > RO_9:										
		# Print the result and compare it to the USA.			
		print(f"U've got {grade}. In USA you would've gotten {USA_A}.")	
else:
	# U can't get more than 10.
	if grade > 10:
		print("You can't get a higher grade than 10.")
	# The lowest grade u can get is 1.
	else:
		print("You can't get a lower grade than 1.")



# (Altfel de) Rezolvare:
# (We'll be using the variables from above).
#Get a grade from the user.
grade = float(input("What grade did u get today: "))
if grade <= 10 and grade > RO_9:
	# Print the result and compare it to the USA.
	print(f"U've got {grade}. In USA you would've gotten {USA_A}.")
elif grade <= RO_9 and grade > RO_8:	
	# Print the result and compare it to the USA.
	print(f"U've got {grade}. In USA you would've gotten {USA_B}.")
elif grade <= RO_8 and grade > RO_7:	
	# Print the result and compare it to the USA.
	print(f"U've got {grade}. In USA you would've gotten {USA_C}.")
elif grade <= RO_7 and grade > RO_6:	
	# Print the result and compare it to the USA.
	print(f"U've got {grade}. In USA you would've gotten {USA_D}.")
elif grade <= RO_6 and grade > RO_4:	
	# Print the result and compare it to the USA.
	print(f"U've got {grade}. In USA you would've gotten {USA_E}.")
elif grade <= RO_4 and grade >= 1:	
	# Print the result and compare it to the USA.
	print(f"U've got {grade}. In USA you would've gotten {USA_F}.")
else:
	# Can't get a higher grade than 10.
	if grade > 10:
		print("You can't get a higher grade than 10.")
	# Can't get a lower grade than 1.		
	elif grade < 1:
		print("You can't get a lower grade than 1. U get 1 for beeing present at the exam.")
			