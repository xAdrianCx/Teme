"""
14. 
avand stringul '0123456789'
afisati doar numerele pare 
acum afisati doar numerele impare
(hint: folositi slicing, controlati din pas)
"""

# Rezolvare:

# Define and initialize the variable.
var = '0123456789'
# Print even numbers.
print(f"Even numbers: {var[::2]}")
# Print odd numbers.
print(f"Odd numbers: {var[1::2]}")

# Just for fun print even numbers in reversed order.
print(f"Reversed even numbers: {var[-2::-2]}")
# Just for fun print odd numbers in reversed order.
print(f"Reversed odd numbers: {var[-1::-2]}")
