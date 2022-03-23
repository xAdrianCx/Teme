"""
6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. False daca nu
"""

# Rezolvare:
def find(x):
	# Return True if a character is in a given string or False if it's not.
	string = "The greatest glory in living lies not in never falling, but in rising every time we fall."
	if x.lower() in string.lower():
		return True
	else:
		return False

print(find("a"))	
print((find("1")))			 
