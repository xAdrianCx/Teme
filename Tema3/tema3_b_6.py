"""
6. 
Folositi o functie care sa stearga lista de la ex3
"""

# Rezolvare:
# Define a list.
l1 = [3, 1, 0, 2, 6, 5, 4]
# CLEARING(not deleting) a list using clear() function.
l1.clear()
# Show that the list has been CLEARED.
print(l1)


# (Altfel de) Rezolvare:
# Define a list.
l1 = [3, 1, 0, 2, 6, 5, 4]
# DELETEING a list.
del l1
# Show that the list has been DELETED(doesn't exist anymore).
# Using an if to catch the error(NameError) we get in case something(a variable) doesn't exist.
if NameError:
	print(f"List 'l1' doesn't exist.")
else:
	print(l1)	
