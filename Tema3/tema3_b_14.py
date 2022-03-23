"""
14.
Afisati diferentele dintre aceste 2 seturi (exercitiu 12)
"""

# Rezolvare:
# Define the given sets.
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
# Find the differences in the 2 sets using an arithmetic operator("-").
dif = zile_sapt - weekend
# Print the differences.
print(f"Diferences between 'zile_sapt' and 'weekend': {dif}")
# find the differences in the 2 sets using difference() functin.
diff = zile_sapt.difference(weekend)
# Show the differences.
print(f"Diferences between 'zile_sapt' and 'weekend': {diff}")