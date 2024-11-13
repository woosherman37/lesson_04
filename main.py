#small app to simulate an interaction between barman and client

print(f"\nHello! What would you like?\n")

order = input(f"We offer latte, americano or cappuccino? ")


price_list = {"latte":4, "americano":3, "cappuccino":3.5}

try:
	price = price_list[order]
	print(f"It's £{price} in total.")	

except KeyError as key:
	print(f"We don't have this item", key)
	






