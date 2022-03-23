"""
19.
citeste un user de la tastatura
citeste o parola
afiseaza: 'Parola pt user x este ***** si are x caractere'
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect
eg: parola abc => ***
parola abcd => ****
"""

# Rezolvare:

# Ask for a username and a password:
user = input("Please, enter your username: ")
password = input("Please, enter your password: ")
# Define a * variable.
pw = "*" * len(password)
# Print user name and password length.
print(f"Parola pt. userul {user} este {pw}, si are {len(password)} caractere.")
