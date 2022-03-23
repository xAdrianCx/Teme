"""
5. 
Clasa Cont

Atribute: iban, titular_cont, sold

Constructor pentru toate

Metode:
afisare_sold() - Titularul x are in contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)
"""

# Rezolvare:
class Account:
	# A class to represent a user account.
	# Constructor.
	def __init__(self, iban, name, balance):
		# Initialize the attributes.
		self.iban = iban
		self.name = name
		self.balance = balance

	def amount(self):
		# A method to show the amount.
		print(f"{self.name} has {self.balance}$ in his account with iban number: {self.iban}.")

	def debit(self, amount):
		# A method to "lose" some money. :)	
		if amount <= self.balance:
			print(f"{amount}$ are beeing withdrawn from the account.")
			print(f"The new account balance is {self.balance - amount}$.")
		else:
			print("Insufficient funds.")	
			
	def credit(self, amount):
		# A method that makes everyone happy(er). :)
		print(f"To the account have been added {amount}$.")
		print(f"The new account balance is {self.balance - amount}$.")

account1 = Account("RO49AAAA1B31007593840000", "Gandalf The Grey", 999999999)
account2 = Account("RO49AABBCC50000551111111", "Geralt of Rivia", 9875455)
account1.amount()
account1.debit(5000000)
account1.credit(999)	
print("____________________________________________________________________")
account2.amount()
account2.debit(5616)
account2.credit(4554)	
print("____________________________________________________________________")
