"""
2.
Verifica si afiseaza daca x este numar pozitiv sau nu.
"""

# Rezolvare:
# Ask for a number.
x = int(input("Enter a number and i will tell you if it's positive." + 
	"\n('True' = positive, 'False' = negative, no answer means u typed '0')" + 
	"\nType your number: "))
# Verify if the number is positive.
if x != 0:
	print((x > 0))


# (Altfel de) Rezolvare: 
# Ask for a number.
x = int(input("Enter a number and i will tell you if it's positive or negative: " + 
	"\n(you are not allowed to type '0')" + 
	"\nType your number: "))
# Verify if the number is positive.
if x != 0 and x > 0:
	print(f"{x} is a positive number.")
# Verify if the number is negative.	
elif x != 0 and x < 0:
	print(f"{x} is a negative number.")
# Print a msg about typing 0.
else:
	print(f"I told you that you are not allowed to type {x}. I quit, goodbye! ")			
