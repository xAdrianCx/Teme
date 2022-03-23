"""
8. 
Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
cititi de la tastatura un int x
afiseaza stringul fara ultimele x caractere
ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
"""

# Rezolvare:

# Define and initialize the variable.
var_str = "Coral is either the stupidest animal or the smartest rock"
# Ask for a number.
num = int(input("Please, enter a number: "))
# Check the length of var_str.
print(f"Length of the given string is {len(var_str)}")
# Print var_str - num(characters).
print(f"String without the last {num} characters: {var_str[:len(var_str) - num]}")
