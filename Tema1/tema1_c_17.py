"""
17.
folosind o singura linie de cod citeste un string de la tastatura (ex: 'alabala portocala')
si salveaza fiecare cuvant intr-o variabila
acum printeaza ambele variabile pentru verificare
"""

# Rezolvare:
# Get a 2-word string from keyboard and store each word in a different variable.
x, y = input("Please, insert a 2-word string: ").split(" ")
# Print the variables.
print(f"In variabila 'x' este stocata valoarea: {x}.")
print(f"In variabila 'y' este stocata valoarea: {y}.")
