"""1.
Avand lista 
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel'] 

Folositi un for ca sa iterati prin toata lista si sa afisati
‘Masina mea preferata este x’
Faceti acelasi lucru cu range-ul listei
Faceti acelasi lucru cu un while
"""

# Rezolvare:
# Define and initialize the given list.
cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# Folositi un for ca sa iterati prin toata lista si sa afisati ‘Masina mea preferata este x’
for car in cars:
	if car == "Mercedes":
		print(f"My favorite car is {car}.")


# Faceti acelasi lucru cu range-ul listei.
for index in range(len(cars)):
	if cars[index] == "Mercedes":
		print(f"My favorite car is {cars[index]}.")


# Faceti acelasi lucru cu un while.
active = len(cars) - 1
while active >= 0:
	active -= 1
	if cars[active] == "Mercedes":
		print(f"My favorite car is {cars[active]}.")
		break


