"""
13.
Ghicitoare de numar
numar_secret = Generati un numar random intre 1 si 30
Numar_ghicit = None
Folosind un while
   User alege un numar
   Programul ii spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitari! Ai ghicit!
"""


# Rezolvare:
# Import the random module.
import random
# Set a random secret number.
secret_number = random.randint(1, 30)
# Set a True flag.
guessed_number = True
while guessed_number:
	# Ask the user to try to guess my secret number.
	chosen_number = int(input("Try to guess my secret number: "))
	# Verify if the guessed number is higher than my secret number.
	if chosen_number > secret_number:
		print("My secret number is lower.")
	# Verify if the guessed number is lower than my secret number.	
	elif chosen_number < secret_number:
		print("My secret number is higher.")
	else:
		# If the numbe isn't higher or lower, it must be the exact number.
		print("Congratulations! You have guessed it!")
		guessed_number = False		
