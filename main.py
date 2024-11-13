#small app to simulate an interaction between barman and client

print(f"\nHello! What would you like?\n")

order = input(f"We offer Latte, Americano or Cappuccino? ")

print(f"\n{order}\n")

if order == "Latte": 
	price = 4
elif order == "Americano":
	price = 3
else:
	price = 3.5

print(f"It's £{price} in total.")





