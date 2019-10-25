my_pizzas = ['pepperoni','margherita']
friend_pizzas = my_pizzas[:]

friend_pizzas.append('meat feast')

print("My favourite pizzas are:")
for pizza in my_pizzas:
    print(pizza.title())

print("My friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())