"""
5. Functie care returneaza aria cercului
"""

# Rezolvare:
from math import pi
def circle_area(radius):
	# Return a circle's area.
	return f"The area of a circle with a radius of {radius} meters is " + "{:.2f}".format(pi * radius * radius) + " square meters."

print(circle_area(50))
print(circle_area(86))	