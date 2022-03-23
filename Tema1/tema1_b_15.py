"""
15. 
Aveti un dreptunghi, declarati 2 variabile pe nume “lungime” si “latime”, 
ele trebuie sa primeasca ca si input de la tastatura dimensiunile.
Printati aria calculata a dreptunghiului
"""

# Rezolvare:

# Teacher note: Este(aproximativ) la fel ca si exercitiul 7.

# Ask for length.
lungime = int(input("Please, enter the length of the rectangle: "))
# Ask for width.
latime = int(input("Please, enter the width of the rectangle: "))
# Print the area of the rectangle.
print("The area of the rectangle is " + str(lungime * latime) + ".")
