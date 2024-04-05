prompt = "Enter the topping you want added to your pizza: "
prompt += "\nPress 'q' when you are done. "

toppings = []
topping = ""


while True:
    topping = input(prompt)
    if topping == 'q':
        break
    toppings.append(topping)

print(f"You wanted the following toppings on your pizza: {toppings}")