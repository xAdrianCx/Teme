"""
11. Functie care primeste o luna din an si returneaza cate zile are acea luna
"""

# Rezolvare:
# Import the modules we need.
from datetime import date
from calendar import monthrange as mr

def month_days(month, year=date.today().year): # Set a default value for year.
	# I know we had to pass only one argument to the function, but seems more usefull this way.
	# Get the number of days in a month by passing the name of the month (and/or(optionally) the year) to the function.
	# 1st make a dict of months so we can use both the name of the month, and index.
	months = {
		"january": 1, "february": 2, "march": 3,
		"april": 4, "may": 5, "june": 6,
		"july": 7, "august": 8, "september": 9,
		"october": 10, "november": 11, "december": 12,
		}	
	# Iterate over dict and get the keys and values.	
	for key, value in months.items():
		if month == str(month):
			if month.lower() == key:
				return f"{key.title()} in {year} has {mr(year, value)[1]} days."
		elif month == int(month):
			if month == value:
				return f"{key.title()} in {year} has {mr(year, value)[1]} days."				
			
print(month_days("FEBRUARY", 2036))	
print(month_days("march", 2059))	
print(month_days(10, 2045))	
print(month_days(11))	
	
	
