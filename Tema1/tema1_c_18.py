"""
18. 
citeste un string de la tastatura (eg: alabala portocala)
salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2 stringuri diferite) 
capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter
=> alAbAlA portocAla
"""

# Rezolvare:

# Ask for a string.
var_string = input("Please, enter a string: ")
# Save the first element into a variable.
var_string1 = var_string[0]
# Print the capitalized version of the string except the 1st and last item.
print(var_string[0] + var_string[1:-1].replace(var_string1, var_string1.capitalize()) + var_string[-1])
