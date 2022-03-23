"""
13.
Folosind variabilele definite la exercitiul numarul 2 (cele 4 variabile declarate de tip str, int, float, bool), 
declarati o alta variabila de tip string in care sa le adaugati folosind tehnica de formatare a unui string.
Printeaza rezultatul.
"""

# Rezolvare:

# A string type variable.
var_str = "Python"
# An int type variable.
var_int = 7
# A float type variable.
var_float = 7.1
# A bool type variable.
var_bool = True

# Define and initialize a variable that contains all defined variables(from above) as one string.
all_to_string = var_str + str(var_int) + str(var_float) + str(var_bool)
# Print the result.
print(all_to_string)
