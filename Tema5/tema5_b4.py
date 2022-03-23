"""
4. Functie care returneaza aria dreptunghiului
"""

# Rezolvare:
def rectangle_area(length, width):
	# Return any rectangle's area.
	# If the user enters a width > length, then that's the length of the rectangle.
	# We make this check so that the return will make sense.
	if width > length:
		length, width = width, length
	return f"The area of a rectangle with length of {length} meters and width of {width} meters is {length * width} square meters."

print(rectangle_area(15, 10))	 
print(rectangle_area(3, 30))