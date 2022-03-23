"""
20. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)
"""

# Rezolvare:
# Import the needed modules.
from datetime import date
def birthday(day, month, year):
	# A function that shows how many days left 'till someone's birtday.
	day = int(day)
	month = int(month)
	year = int(year)
	birthday = date(year, month, day)
	today = date.today()
	return f"Days left 'till my birthday: {(birthday - today).days}."
print(birthday(26, 11, 2022))	
print(birthday(23, 8, 2022))	
print(birthday(11, 7, 2022))	