"""
3. Functie care returneaza numarul total de caractere din numele tau complet.
(nume, prenume, nume_mijlociu) 
"""

# Rezolvare: 
def num_of_chars_ws(name):
	# Return the number of characters in a name including white spaces(ws).
	return f"Number of characters in your full name including white spaces: {str(len(name))}."
	

def num_of_chars_no_ws(name):	
	# Return the number of characters in a name excluding white spaces(no_ws).
	name_no_ws = " ".join(name).split()
	return f"Number of characters in your full name excluding white spaces: {str(len(name_no_ws))}."	


print(num_of_chars_ws('Cotuna Adrian'))
print(num_of_chars_no_ws("Cotuna Adrian"))
