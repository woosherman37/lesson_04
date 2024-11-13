#small app to simulate an interaction between barman and client

print(f"\nHello! What would you like?\n")

order = input(f"We offer Latte, Americano or Cappuccino? ")

print(f"\n{order}\n")


price_list = {"latte":4, "americano":3, "cappuccino":3.5}

price = price_list[order]


print(f"It's £{price} in total.")





