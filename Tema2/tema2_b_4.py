"""
4. 
Verifica si afiseaza daca x este intre -2 si 13
"""

# Rezolvare:

# Ask for a number.
x = int(input("Enter a number and i will tell you if it's in between -2 and 13: "))
# Store the 2 given numbers into variables.
y = -2
z = 13
# Verify if x is in between the given numbers or not.
if x > y and x < z:
	print(f"Yes, {x} is in between {y} and {z}.")
else:
	print(f"{x} is not in between {y} and {z}")


# (Altfel de) Rezolvare:
# Ask for a number.
x = int(input("Enter a number and i will tell you if it's in between -2 and 13: " + 
	"\n('True' = it is in between -2 and 13, 'False' = it's not)" + 
	"\nType your number: "))
# Store the 2 given numbers into variables.
y = -2
z = 13
# Verify if x is in between the given numbers or not.
print(x < 13 and x > -2)
