"""
7. Clasa TodoList
 
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor

Metode:
--> adauga_task(nume, descriere) - se va adauga in dict
--> finalizeaza_task(nume) - se va sterge din dict
--> afiseaza_todo_list() - doar cheile
--> afiseaza_detalii_suplimentare(nume_task) - in functie de numele taskului printam detalii suplimentare, daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
Daca acesta raspunde nu - la revedere
daca raspunde da - il cerem detalii task si salvam nume+detalii in dict

"""

# Rezolvare:
class ToDoList:
	# A class to represent a todo list.
	# Define a dict.
	todo = {}

	def add_task(self, name, description):
		# A method to add a task into our dict.
		self.todo[name] = description

	def finish_task(self, name):
		# A method to finish a task.
		print(f"Finished task '{self.todo[name]}'.")
		self.todo.pop(name)

	def display_keys(self):
		# A method to display the keys in our dict.
		print(list(self.todo.keys()))

	def details(self, name):
		# A method to show the description of a task.
		if name in self.todo.keys():
			print(f"Task {name} has the following details: {self.todo[name]}.")
		else: 
			# If task not in dict.
			answer = input(f"{name} is not in the task list. Would u like to add it?" + "\nType 'yes' or 'no' " )
			if answer.lower() == "yes":
				# Add task to dict.
				self.todo[name] = input("Input some details: ")
				print(f"Task {name} has the following details: {self.todo[name]}.")
			else:
				print("Nothing new added to the list. Goodbye!")	
	
our_list1 = ToDoList()
our_list2 = ToDoList()
our_list1.add_task(1, "Buy bread.")
our_list1.add_task(2, "Play tennis.")
our_list1.add_task(3, "Make a pie.")
our_list1.add_task(4, "Go to the store.")
print(our_list1.todo)
our_list1.finish_task(2)
print(our_list1.todo)
our_list1.details(3)
print(our_list1.todo)
print("____________________________________________________________________________________________")
our_list2.add_task(1, "Order pizza at 17:00.")
our_list2.add_task(2, "Dentist appointment at 18:30.")
our_list2.add_task(3, "Check e-mails.")
our_list2.add_task(4, "Order cinema tickets.")
print(our_list2.todo)
our_list2.finish_task(2)
print(our_list2.todo)
our_list2.details(7)
print(our_list2.todo)
print("____________________________________________________________________________________________")
