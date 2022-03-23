"""
12.
Set
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
Adaugati in zilele_sapt ‘luni’
Afisati zile_sapt
"""

# Rezolvare:
# Defining the given set.
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# Change the set to a list so that we can modify it.
zile_sapt = list(zile_sapt)
# Adding luni to the list.
zile_sapt.append('luni')
# Show the list.
print(zile_sapt)
# Changing back to a set.
zile_sapt = set(zile_sapt)
# Show the set.
print(zile_sapt)
