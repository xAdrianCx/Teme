"""
13.
Folositi un if si verificati daca 
Weekend este un subset al zilelor din sapt
Weekend nu este un subset al zilelor din sapt
"""

# Rezolvare:
# Define the given sets.
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
# Verify if weekend is or not a subset of zile_sapt.
if weekend in zile_sapt:
	# If weekend is a subset of zile_sapt print that.
	print(f"The set: {weekend} is a subset of the set:  {zile_sapt}.")
else:
	# If it gets out of if, then weekend is not a subset of zile_sapt.
	print(f"The set: {weekend} is NOT a subset of the set:  {zile_sapt}.")
	