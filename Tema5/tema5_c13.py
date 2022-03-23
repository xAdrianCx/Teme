"""
13. Functie care primeste o lista de cifre (adica doar 0-9)
Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returneaza un DICT care ne spune de cate ori apare fiecare cifra.
=> dict {
0: 0
1: 2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
"""

# Rezolvare:
def count_nums(nums):
	# A function that receives a list of nums and returns a dictionary
	# that shows how many times each number appears in the list.
	dict_count = {}
	for i in range(0, 10):
		dict_count[i] = nums.count(i)
	# To keep the resulting given format we need to print(not return) the dict_count.
	for i, j in dict_count.items():
		print(f"{i}: {dict_count[i]}")
count_nums([1, 3, 1, 5, 9, 7, 7, 5, 5])
print("_________________________________")
count_nums([2, 2, 3, 4, 4, 4, 7, 7, 9])
print("_________________________________")
count_nums([9, 9, 9, 9, 9, 9, 9, 9, 9])

		