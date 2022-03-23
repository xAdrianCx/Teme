"""
6.
Clasa Masina

Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate masinile cand ies din fabrica sunt gri
Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
Culori disponibile = alegeti voi 5-7 culori
Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
Inmatriculata = False

Constructor: model, viteza_maxima

Metode:
descrie() (se vor printa toate atributele, inafara de culori_disponibile)
inmatriculare() - va schimba atributul inmatriculata in True
vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori disponibile, altfel afisati o eroare
accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
franeaza() - masina se va opri si va avea viteza 0
"""

class Car:
	# A class to represent a car.
	make = "Volvo"
	actual_speed = 0
	color = "Grey"
	available_colors = {"Grey", "Red", "Blue", "Green", "Orange", "Yellow", "Brown"}
	registered = False

	# Constructor
	def __init__(self, model, max_speed):
		# Initialize the attributes.
		self.model = model
		self.max_speed = max_speed

	def describe(self):
		# A method that describes a car.
		print(f"The car is a {self.color} {self.make} {self.model}." + 
			f"\nIt's actual speed is {self.actual_speed}Km/h, but it can get up to {self.max_speed}Km/h." + 
			f"\n......oh, and it's registration status for now is: {self.registered}.")	

	def register(self):
		# A method to register a car.
		self.registered = True

	def paint(self, color):
		# A method to paint a car.
		if color in self.available_colors:
			self.color = color
			print(f"Choosing a color for the car..." + 
				f"The car has been painted {self.color}.")
		else:
			print(f"Choosing a color for the car..." +
				"Color not available.")

	def accelerate(self, speed):
		# a method to accelerate a car.
		if speed < 0:
			print("You can't go slower than beeing still.")
		elif speed > self.max_speed:
			self.actual_speed = self.max_speed
			print(f"Accelerating to {self.actual_speed}Km/h.")
		else:
			self.actual_speed = speed
			print(f"Accelerating to {self.actual_speed}Km/h.")

	def stop(self):
		# A method to stop a car			
		self.actual_speed = 0
		print(f"Hitting the breaks. Car's current speed is {self.actual_speed}Km/h.")

car1 = Car("S60", 260)
car2 = Car("S90", 300)
car1.describe()
car1.register()
car1.paint("Magenta")
car1.paint("Orange")
car1.accelerate(130)
car1.accelerate(300)
car1.stop()
print("______________________________________________________________________")
car2.describe()
car2.register()
car2.paint("Magenta")
car2.paint("Brown")
car2.accelerate(130)
car2.accelerate(300)
car2.stop()
print("______________________________________________________________________")
