"""
15.
Afisati intersectia elementelor din aceste 2 seturi (exercitiu 12)
"""

# Rezolvare:
# Define the given sets.
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
# Find the intersection of the 2 sets.
intersection = zile_sapt.intersection(weekend)
# Show the intersection.
print(f"Intersection of 'zile_sapt' with 'weekend': {intersection}")
