"""
5. 
Modernizati parcul de masini
Creati o lista goala, masini_vechi
Iterati prin masini
Cand gasiti Lastun sau Trabant:
Salvati aceste masini in masini_vechi
Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
Printati Modele vechi: x
Modele noi: x
"""

# Rezolvare:
# Define and initialize the given list.
cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
old_cars = []

# Search for "Trabant" and "Lastun" in cars, add them to old_cars and replace them in cars with "Tesla".
for i in range(len(cars)):
	if cars[i] == "Trabant" or cars[i] == "Lastun":
		old_cars.append(cars[i])
		cars[i] = "Tesla" 
# Show the result.		
print(f"New models: {cars}")
print(f"Old models: {old_cars}")	


# List comprehension.
cars_2 = cars + [cars[i] == "Tesla" for i in range(len(cars)) if cars[i] == "Trabant" or cars[i] == "Lastun"]
old_cars2 = [old_cars2.append(cars[i]) for i in range(len(cars)) if cars[i] == "Trabant" or cars[i] == "Lastun"], 
					
print(f"New models 2 : {cars_2}")
print(f"Old models 2 : {old_cars}")