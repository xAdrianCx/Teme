"""
ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’
"""

# Rezolvare:
# Import abc module to declare an abstract class.
from abc import ABC, abstractmethod


class GeometricShape(ABC):
    pi = 3.14

    @abstractmethod
    def area(self):
        # Abstract method.
        pass

    def describe(self):
        # Normal method.
        print("Most probably, i have corners.")


"""
INHERITANCE
Clasa Patrat - mosteneste FormaGeometrica
constructor pt latura
ENCAPSULATION
latura este proprietate privata
Implementati getter, setter, deleter pt latura
Implementati metoda ceruta de clasa abstracta
"""


class Square(GeometricShape):
    # Constructor
    def __init__(self, side):
        self.__side = side

    # Get the value of the side of the square.
    def get_side(self):
        print("Getting the side of the square...")
        return f"We have a square with a side of: {self.__side}"

    # Set a value to side of a square.
    def set_side(self, value):
        print("Setting a new side to our square...")
        self.__side = value

    # Delete the value of side.
    def del_side(self):
        print(f"Deleting the side of the square...")
        self.__side = 0
        pass



    # Abstract method.
    def area(self):
        # Return the area of a square.
        return f"The area of a square with the side of {self.__side} is {self.__side * self.__side}"


"""Clasa Cerc - mosteneste FormaGeometrica
constructor pt raza
raza este proprietate privata
Implementati getter, setter, deleter pt raza
Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte
"""


class Circle(GeometricShape):
    # Constructor
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        print(f"The radius of the circle is {self.__radius}")
        return self.__radius

    @radius.getter
    def radius(self):
        return f"The radius of the circle is {self.__radius}"

    @radius.setter
    def radius(self, value):
        print(f"Setting a new radius to the circle...")
        self.__radius = value

    @radius.deleter
    def radius(self):
        print("Deleting the circle's radius value...")
        self.__radius = 0

    def area(self):
        return f"The area of a circle with the radius of {self.__radius} is {self.pi * (self.__radius ** 2)}"
    """
    POLYMORPHISM 
    Definiti o noua metoda descrie() - printati ‘Eu nu am colturi’
    """
    def describe(self):
        print("I've got no corners.")


"""
Creati un obiect de tip Patrat si jucati-va cu metodele lui
Creati un obiect de tip Cerc si jucati-va cu metodele lui
"""

obj_square = Square(50)
obj_circle = Circle(20)
obj_square.describe()
print(obj_square.get_side())
print(obj_square.area())
obj_square.set_side(90)
print(obj_square.get_side())
print(obj_square.area())
obj_square.del_side()
print(obj_square.get_side())
print(obj_square.area())
print("___________________________________________________")
obj_circle.describe()
print(obj_circle.radius)
print(obj_circle.area())
obj_circle.radius = 60
print(obj_circle.radius)
print(obj_circle.area())
del obj_circle.radius
print(obj_circle.radius)
print(obj_circle.area())