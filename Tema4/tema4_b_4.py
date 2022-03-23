"""
4.
Aceasi lista
Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun. 
Daca masina e Trabant sau Lastun
   Folositi un cuvant cheie care sa dea skip la ce urmeaza
(nu trebuie else)
Printati S-ar putea sa va placa masina x
"""

# Rezolvare: 
# Define and initialize the given list.
cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for i in cars:
	if i == "Trabant" or i == "Lastun":
		continue
	print(f"You might like the car {i}.")