"""
12.
Aceeasi lista
Ordonati crescator lista fara sa folositi sort
Va puteti inspira vizual de aici
https://www.youtube.com/watch?v=lyZQPjUT5B4
"""

# Rezolvare:
# Define the given list.
other_numbers = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# Iterate over the list.
for i in range(len(other_numbers)):
	# Iterate over another list which starts at index 1 of the first list.
	for j in range(i + 1, len(other_numbers)):
		# verify if the 1st number is higher than the second.
		if other_numbers[i] > other_numbers[j]:
			# If the 1st number is higher than the second, swap them.
			other_numbers[i], other_numbers[j] = other_numbers[j], other_numbers[i]
print(other_numbers)					



# (Altfel de) Rezolvare:
# Define a new list to store a sorted current list.
sorted_numbers = []
for i in other_numbers.copy():
	i = min(other_numbers)
	sorted_numbers.append(i)
	other_numbers.remove(i)
print(sorted_numbers)	
