"""
5. 
folositi print() si printati in consola 4 propozitii folosind cele 4 variabile. 
(rezolvati nepotrivirile de tip prin ce modalitate doriti)
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
# "Rounding" var_float.
var_float1 = round(var_float)

# Using the f string.
# Using var_str in a sentence.
print(f"We love studying {var_str}.")
# Using var_int.
print(f"{var_int} is my favorite number.")
# Using var_float.
print(f"If we use 'round()' function on {var_float} we get {var_float1}.")
# Using var_bool.
print(f"It is {var_bool} that we love studying {var_str}.")

# Using conventional mode.
# Using var_str in a sentence.
print("We love studying " + var_str + ".")
# Using var_int.
print(str(var_int) + " is my favorite number.")
# Using var_float.
print("If we use 'round()' function on " + str(var_float) + " we get " + str(var_float1) + ".")
# Using var_bool.
print("It is " + str(var_bool) + " that we love studying " + var_str + ".")
