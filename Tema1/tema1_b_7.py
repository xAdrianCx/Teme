"""
7. 
citeste de la tastatura lungimea
citeste de la tastatura latimea
afiseaza 'Aria dreptunghiului este x'
"""

# Rezolvare:

# Ask for length.
length = int(input("Please, enter the length of the rectangle: "))
# Ask for width.
width = int(input("Please, enter the width of the rectangle: "))
# Print the area of the rectangle using conventional mode.
print("The area of the rectangle is " + str(length * width) + ".")
# Print the area of the rectangle using the 'f' string.
print(f'The area of the rectangle is {str(length * width)}.')
