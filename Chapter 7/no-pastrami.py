sandwich_orders = ['tuna', 'pastrami', 'turkey', 'pastrami','roast beef', 'rueben', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"I have made the {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print(f"The following sandwiches have been completed:\n")
print(finished_sandwiches)
