"""
1. 
Clasa Cerc

Atribute: raza, culoare

Constructor pt ambele atribute

Metode:
descrie_cerc() - va PRINTA culoarea si raza
aria() - va RETURNA aria 
diametru() 
circumferinta()
"""

# Rezolvare:
from math import pi
class Circle:
	# A class to represent a circle.
	# Constructor.
	def __init__(self, radius, color):
		# Initialize the attributes.
		self.radius = radius
		self.color = color

	def describe(self):
		# A method that prints the radius and color of a circle.
		print(f"The circle's radius is {self.radius} and its color is {self.color}.")

	def area(self):
		# A method that returns a circle's area.
		return "{:.2f}".format(pi * self.radius * self.radius)

	def diameter(self):
		# A method that returns the diameter of a circle.
		return self.radius * 2

	def circumference(self):
		# A method that returns a circle's circumference.
		return "{:.2f}".format(2 * pi * self.radius)	

circle1 = Circle(50, "Green")
circle2 = Circle(96, "Yellow")
circle1.describe()
print(f"1st circle has an area of: {circle1.area()} square meters.")
print(f"1st circle has a diameter of: {circle1.diameter()}.")			
print(f"1st circle has a circumference of: {circle1.circumference()} meters.")
print("_____________________________________________________________________________")	
circle2.describe()
print(f"2nd circle has an area of: {circle2.area()} square meters.")
print(f"2nd circle has a diameter of: {circle2.diameter()}.")			
print(f"2nd circle has a circumference of: {circle2.circumference()} meters.")	
print("_____________________________________________________________________________")	
