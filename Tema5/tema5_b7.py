"""
7. Functie fara return, primeste un string si printeaza pe ecran:
Nr de caractere lower case este x
Nr de caractere upper case este y 
"""

# Rezolvare:
def lower_upper(string):
	# Print how many upper or lower case characters are in a string.
	count_lower = 0
	count_upper = 0
	alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	random = []
	for i in alphabet:
		for j in string:
			if j == i:										
				count_lower += 1
			elif j == i.upper():
				count_upper += 1
	print(f"Number of lowercase characters: {str(count_lower)}.")
	print(f"Number of uppercase characters: {str(count_upper)}.")
lower_upper("Adrian CotunA")
lower_upper("ADRIAN cotuna 32")	