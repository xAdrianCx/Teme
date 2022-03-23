"""
2. 
Clasa Dreptunghi

Atribute: lungime, latime, culoare

Constructor pt toate atributele

Metode:
descrie() va PRINTA lungime, latime, culoare
aria()
perimetrul()
schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. 
Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. 
Puteti verifica schimbarea culorii prin apelarea metodei descrie().
"""

# Rezolvare:
class Rectangle:
	# A class to represent a rectangle.
	# Constructor.
	def __init__(self, length, width, color):
		# Initialize the attributes.
		self.length = length
		self.width = width
		self.color = color

	def describe(self):
		# A method that prints the length, width and color of a rectangle.
		print(f"This rectangle has a length of {self.length}, a width of {self.width} and its color is {self.color}.")

	def area(self):
		# A method that returns the area of the rectangle.
		return self.length * self.width

	def perimeter(self):
		# A method that returns the perimeter of a rectangle.
		return (self.length * 2) + (self.width * 2)			

	def new_color(self, new_color):
		self.color = new_color

rectangle1 = Rectangle(50, 20, "Blue")
rectangle2 = Rectangle(500, 60, "Green")	
rectangle1.describe()		
print(f"The area of 1st rectangle is {rectangle1.area()} square meters.")
print(f"The perimeter of 1st rectangle is {rectangle1.perimeter()} meters.")
rectangle1.new_color("Red")
rectangle1.describe()
print("_________________________________________________________________________")
rectangle2.describe()		
print(f"The area of 2nd rectangle is {rectangle2.area()} square meters.")
print(f"The perimeter of 2nd rectangle is {rectangle2.perimeter()} meters.")
rectangle2.new_color("Grey")
rectangle2.describe()
print("_________________________________________________________________________")
