"""
4.
Clasa Factura

Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc

Constructor: toate atributele, fara serie

Metode:
schimba_cantitatea(cantitate)
schimba_pretul(pret)
schimba_nume_produs(nume)
genereaza_factura() - va printa tabelar daca reusiti

Factura seria x numar y
Data: generati automat data de azi
Produs | cantitate | pret bucata | Total “
Telefon |      7       |       700       | 49000     

Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/
"""

# Rezolvare:
from datetime import date
class Invoice:
	# A class to represent an invoice.
	invoice_series = "INV18032022"
	#Constructor
	def __init__(self, number, product, quantity, unit_price):
		# Initialize the attributes.
		self.number = number
		self.product = product
		self.quantity = quantity
		self.unit_price = unit_price

	def change_quantity(self, quantity):
		# A method that changes quantity.
		self.quantity = quantity

	def change_price(self, price):
		# A method that changes the price.
		self.unit_price = price		

	def change_product(self, product):
		# A method that changes the product.
		self.product = product

	def generate_invoice(self):
		# A method to generate the invoice.
		# Store the invoice headers in a list.
		invoice_headers = ["| PRODUCT ", " | QUANTITY ", " | UNIT PRICE ", " | TOTAL"]
		# Store the invoice values in a list.	
		invoice_values = ["| " + str(self.product), " | " + str(self.quantity), " | " + str(self.unit_price), " | " + str((self.quantity * self.unit_price))]
		# Iterate over headers.
		for i in range(len(invoice_headers)):
			# Iterate over values.
			for j in range(i, i + 1):
				# If the length of header is smaller than value's, make them the same size.
				if len(invoice_headers[i]) < len(invoice_values[j]):
					invoice_headers[i] = invoice_headers[i] + (len(invoice_values[j]) - len(invoice_headers[i])) * " "
					break
				# If the length	of the value is smaller than header's, make them the same size.
				elif len(invoice_values[j]) < len(invoice_headers[i]):
					invoice_values[j] = invoice_values[j] + (len(invoice_headers[i]) - len(invoice_values[j])) * " "	
					break			
		# Print the invoice neatly formatted.			
		invoice_headers.append(" |")
		invoice_values.append(" |")
		print(f"Invoice series {self.invoice_series}, NR. {self.number}" + 
			f"\nDate: {date.today()}")			
		print(* invoice_headers)
		print(* invoice_values)

			
invoice1 = Invoice(23, "Mouse", 2, 50)	
invoice2 = Invoice(196, "Laptop", 1, 2500)	
invoice1.generate_invoice()
print("__________________________________________________________________________________________________")
# Apply changes to the invoice1.
invoice1.change_quantity(3)
invoice1.change_price(40)
invoice1.change_product("Mechanical Keyboard")
invoice1.generate_invoice()
print("__________________________________________________________________________________________________")
invoice2 = Invoice(196, "Laptop", 1, 2500)	
invoice2.generate_invoice()
print("__________________________________________________________________________________________________")
# Apply changes to the invoice2.
invoice2.change_quantity(3)
invoice2.change_price(200000000333333333300)
invoice2.change_product("Asus gaming headphones")
invoice2.generate_invoice()
print("__________________________________________________________________________________________________")
