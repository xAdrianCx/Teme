"""
9. 
Citeste o litera de la tastatura
Verifica si afiseaza daca este vocala sau nu
"""

# Rezolvare:
# Define a variable containing all the vowels.
vowels = "aeiou"   	
# Ask the user for a random letter.																												
vowel = input("Give me a letter and i will tell you if it's a vowel or not" + 
	"\nChoose a letter: ")   
# Verify if the typed letter is at any index of 'vowels'	
# and if it is, print the result.																									
if (vowel.lower() == vowels[0].lower() or vowel.lower() == vowels[1].lower()
		or vowel.lower() == vowels[2].lower() or vowel.lower() == vowels[3].lower()
		or vowel.lower() == vowels[-1].lower()):			
	print(f"'{vowel}' is a vowel.")  
# If it gets out from the if statement it's not a vowel.	 																								
else:				
# Print the result.																												
	print(f"'{vowel}' is not a vowel.")																								


# (Altfel de) Rezolvare:
# Define a variable containing all the vowels.
vowels = "aeiou"   	
# Ask the user for a random letter.																												
vowel = input("Give me a letter and i will tell you if it's a vowel or not" + 
	"\nChoose a letter: ")  
# Verify if the typed letter is in 'vowels'
# and print the result only if it is a vowel.																											
if vowel.lower() in vowels.lower():   																								
	print(f"'{vowel}' is a vowel.") 
# If it gets out from if it means it's not a vowel.	  																								
else:   
	# Print the result.																															
	print(f"'{vowel}' is not a vowel.")   																							
	