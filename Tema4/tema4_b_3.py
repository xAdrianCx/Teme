"""
3. 
Aceeasi lista, 
Vine un cumparator care doreste sa cumpere un Mercedes
Iterati prin ea prin for each
Daca masina e mercedes (if)
   Printam ‘am gasit masina dorita de dvs’
   Iesim din ciclu folosind un cuvant cheie care face acest lucru
Altfel (else apartine de if, nu de for)
   Printam Am gasit masina X. Mai cautam
"""

# Rezolvare: 
# Define and initialize the given list.
cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for i in cars:
	if i == "Mercedes":
		print(f"We have found the car you wanted. It's {i}.")
		break	
	else:
		print(f"We have found the car {i}.")	
