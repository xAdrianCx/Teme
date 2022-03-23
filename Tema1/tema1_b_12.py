"""
12.
acelasi string
salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
(hint: este o functie care te ajuta sa faci asta)
folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
output: 'Coral is either the stupidest animal or the smartest ' 
"""

# Rezolvare:

# Define and initialize the variable.
var_str = "Coral is either the stupidest animal or the smartest rock"
# Save to a variable the start index of word 'rock.'
rock_index = var_str.index('rock')
# Print var_str until 'rock'.
print(var_str[:rock_index])
