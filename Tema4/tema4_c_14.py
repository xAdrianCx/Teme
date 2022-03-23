"""
14. 
Alegeti un numar de la tastatura
Ex:7
Scrieti un program care sa genereze in consola urmatoarea piramida
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
"""

# Rezolvare:
# Ask the user for a number.
number = int(input("Give me a number: "))
# Iterate over the given range and print each number as many times as the iteration.
for i in range(number + 1):
	print(f"{i}" * i)



