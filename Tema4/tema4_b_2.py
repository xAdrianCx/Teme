"""2.
Aceeasi lista
Folositi un for else
In for
   Modificati elementele din lista astfel incat sa fie scrise cu majuscule, exceptand primul si ultimul
In else 
   Printati lista
"""

# Rezolvare: 
# Define and initialize the given list.
cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for index in range(1, len(cars) - 1):
	cars[index] = cars[index].upper()
print(cars)	


# List comprehension.
print([cars[0]] + [cars[index].upper() for index in range(1, len(cars) - 1)] + [cars[-1]])
		
 