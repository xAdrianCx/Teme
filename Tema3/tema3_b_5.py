"""
5. 
Folosind un if verificati lista generata la ex3 si afisati:
-Lista este goala
-Lista nu este goala
"""

# Rezolvare:
# Define a list.
l1 = [3, 1, 0, 2, 6, 5, 4]
# Verify if the list is empty
if len(l1) < 1:
	# Show if a list is empty.
	print("List is empty.")
	# If it get's out of if, the list is not empty.
else:
	print("List isn't empty.")	
	