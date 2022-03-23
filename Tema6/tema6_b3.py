"""
3.
Clasa Angajat

Atribute: nume, prenume, salariu

Constructor() pt toate atributele // constructor reprezinta __init__

Metode:
descrie() print nume, prenume, salariu
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
"""

# Rezolvare:
class Employee:
	# A class to represent an employee.
	# Constructor.
	def __init__(self, first, last, salary):
		# Initialize the attributes.
		self.first = first
		self.last = last
		self.salary = salary

	def describe(self):
		# A method to display the details of the employee.
		print(f"First name: {self.first}.")
		print(f"Last name: {self.last}.")
		print(f"Salary: {self.salary}.")

	def full_first(self):
		# A method to display the full first of the employee.
		print(f"Employee's full first: {self.first + ' ' + self.last}.")

	def monthly_income(self):
		# A method to display the monthly income.
		print(f"{self.first + ' ' + self.last} earns {self.salary} every month.")

	def annual_income(self):
		# A method to display the annual income.
		print(f"{self.first + ' ' + self.last} earns {self.salary * 12} every year.")

	def raise_salary(self, percentage):
		# A method that gives a raise.
		self.percentage = percentage
		self.salary = self.salary + (self.percentage / 100) * self.salary
		print(f"{self.first + ' ' + self.last} has gained a {percentage}% raise. He earns now {self.salary:.2f} every month.")

employee1 = Employee("Adrian", "Cotuna", 3500)
employee2 = Employee("Lionel", "Messi", 3416666.67)
employee1.describe()
employee1.monthly_income()
employee1.annual_income()
employee1.raise_salary(50)	
print("____________________________")
employee2.describe()
employee2.monthly_income()
employee2.annual_income()
employee2.raise_salary(39.4)	
print("____________________________")
