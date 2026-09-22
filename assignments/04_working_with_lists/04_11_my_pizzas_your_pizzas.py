'''
Mike Goodman Pizza Pizza 
'''
pizzas = ["Pepperoni", "Cheese", "Veggie"]
friend_pizzas = pizzas[:]

pizzas.append("Hawaiian")
friend_pizzas.append("cheese")

print("My favorite pizzas are pepperoni, supreme:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are cheese, chicken:")
for pizza in friend_pizzas:
    print(pizza)