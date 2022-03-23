"""
9.
acelasi string
declara un string nou care sa fie format din primele 5 caractere + ultimele 5
"""

# Rezolvare:

# Define and initialize the variable.
var_str = "Coral is either the stupidest animal or the smartest rock"
# Making a new string containing the first and last 5 elements(concatenated) from var_str.
var_5_5 = var_str[:5] + var_str[-5:]
# Print the first 5 elements + the last 5 elements in var_str.
print(f"If we concatenate the first and last 5 elements from the string 'var_str' we get: {var_5_5}")
