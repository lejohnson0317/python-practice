my_pizzas = ['pepperoni', 'cheese', 'sausage']
friends_pizzas = my_pizzas[:]

my_pizzas.append("meat lovers")
friends_pizzas.append("veggie lovers")

print("My favorite pizzas are:")
for pizza in my_pizzas:
     print(f"- {pizza}")

print ("My friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(f"- {pizza}")