"""
c. Optionale (may need google)
16. 
citeste de la tastatura un string de dimensiune impara
afiseaza caracterul din mijloc
"""

# Rezolvare:

# Ask the user for an odd string.
odd_string = input("Please, enter an odd string: ")
# Print the middle elemnt in the string.
print(f"The middle element in '{odd_string}' is: {odd_string[int((len(odd_string)-1)/2)]}")
