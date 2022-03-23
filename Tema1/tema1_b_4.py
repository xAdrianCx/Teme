"""
4. 
Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere)
Verificati tipul acesteia.
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

# Verificam valoarea variabilei var_float inainte de modificare.
print(var_float)
# Verificam tipul variabilei var_float inainte de a o modifica.
print("Variabila 'var_float' este de tipul: " + str(type(var_float)))
# Modificam variabila var_float:
var_float = round(var_float)
# Verificam valoarea variabilei var_float dupa modificare.
print(var_float)
# Verificam tipul variabile var_float.
print("Dupa suprascriere, variabila 'var_float' este de tipul: " + str(type(var_float)))
