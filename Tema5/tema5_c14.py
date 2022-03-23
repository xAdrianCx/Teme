"""
14. Functie care primeste 3 numere
Returneaza valoarea maxima dintre ele
"""

# Rezolvare:
def max_num(x, y, z):
	# A function that receives 3 numbers and returns the highest number.
	return max(x, y, z)
print(max_num(10, 4, 6))
print(max_num(30, 44, 53))
print(max_num(-10, -20, -30))


# (Altfel de) Rezolvare:
def max_number(x, y, z):
	# A function that receives 3 numbers and returns the highest number
	# Store the 3 given numbers into a list
	nums = [x, y, z]
	# Sort the list ascending.
	for i in range(0, len(nums)):
		for j in range(i + 1, len(nums)):
			if nums[i] > nums[j]:
				nums[i], nums[j] = nums[j], nums[i]
	# Get the highest item in the sorted list(which is the last one).			
	highest = nums[-1]			
	# Return the highest number in the list.
	return highest			
print(max_number(10, 4, 6))
print(max_number(30, 44, 53))
print(max_number(-10, -20, -30))