"""
3.
Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
Gasiti 2 variante sa le uniti intr-o singura lista. 
"""

# Rezolvare:
# Define 2 variables for our given lists.
l1 = [3, 1, 0, 2]
l2 = [6, 5, 4]
# Combine the 2 lists by concatenation.
l3 = l1 + l2
# Show the result.
print(l3)
# Combine the 2 lists using extend() method.
l1.extend(l2)
# Show th result.
print(l1)
