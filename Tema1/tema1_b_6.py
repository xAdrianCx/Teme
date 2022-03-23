"""
6. 
citeste de la tastatura numele
citeste de la tastatura prenumele
afiseaza 'Numele complet are x caractere'
"""

# Rezolvare:

# Ask for first name.
first_name = str(input("Please, enter your first name: "))
# Ask for last_name.
last_name = str(input("Please, enter your last name: "))
# Print the length of full name using conventional mode.
print("Numele tau complet are " + str((len(first_name) + len(last_name))) + " caractere.")
# Print the length of full name using the 'f' string.
print(f'Numele tau complet are {str((len(first_name) + len(last_name)))} caractere.')
