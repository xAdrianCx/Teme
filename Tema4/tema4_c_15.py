"""
15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterati prin lista 2d
Printati ‘Cifra curenta este x’
(hint: nested for - adica for in for)
"""


# Rezolvare:
# Define the given list.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
# Iterate over the list.
for i in tastatura_telefon:
	# Iterate over each list in our list.
	for j in i:
		print(f"Current number is: {j}.")
		