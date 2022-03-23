"""
15. X, y, z - reprezinta unghiurile unui triunghi
Verifica si afiseaza daca triunghiul este valid sau nu
"""

# Rezolvare: 
# Ask the user for 3 angle measurements.
x = int(input("Give me the 3 angle measurements of a triangle and" + 
	"\ni will tell you if the triangle is valid." + 
	"\nType the 1st angle: "))															
y = int(input("Type the 2nd angle: "))														
z = int(input("Type the 3rd angle: "))
if x + y + z == 180:	
	# If the sum of angles in a triangle is 180
	# print that the triangle is valid.																 
	print(f"The triangle with angle measurements of {x}, {y} and {z} " + 								
		"\nis a valid triangle.")														
else:		
	# If the sum of angles in a triangle is not 180
	# print that the triangle is not valid.																			
	print(f"The triangle with angle measurements of {x}, {y} and {z} " + 					
		"\nis not a valid triangle.")	
