"""
8. 
X, y, z - laturile unui triunghi
Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
"""

# Rezolvare:
# Ask the user for 3 numbers(sides of a triangle.)										
x = int(input("Give me the length of the 3 sides of a triangle " + 
	"\nand i will tell you the type of the triangle." +                 	
	"\nEnter the length of the 1st side: "))
y = int(input("Enter the length of the 2nd side: "))
z = int(input("Enter the length of the 3rd side: "))
# Make sure all sides are different.
if x != y != z != x:  												
	# Scalene. 		
	print("A triangle with 3 different sides is a SCALENE TRIANGLE.") 
# Make sure any 2 sides are equal(3rd side must be different or it's gonna be equilateral).	  	  
elif x == y and x != z or x == z and x != y or y == z and y != x:
	# Isosceles.   		
	print("A triangle with 2 equal sides is an ISOSCELES TRIANGLE.")   	
# If it gets out from ifs, it means all sides are equal.		 
else:    													
	 # Equilateral.				
	print("A triangle with all sides equal is an EQUILATERAL TRIANGLE.")   
