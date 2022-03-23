"""
18. Functie care sa aplice o reducere de pret
Daca produsul costa 100 lei si aplicam reducere de 10%
Pretul va fi 90
Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida
"""

# Rezolvare:
# Import the needed modules to work with decimal values.
def price_discount(price, discount):
	# Function that receives a price and a discount and returns a price with applied discount.
	# If the discount is higher than 100%, then the product is free of charge.
	if discount >= 100.00:
		return f"After applying a {discount}% discount on a price of {price}$, the product is free of charge, enjoy! :)"	
	else:
		new_price = price - (discount / 100 * price)
		return f"After applying a {float(discount)}% discount on a price of {price}$, you need to pay only" + " {:.2f}".format(new_price) + "$."
print(price_discount(100, 70))
print(price_discount(230.45, 37.56))				
print(price_discount(88500.50, 46.79))
print(price_discount(7500.50, 100.02))
