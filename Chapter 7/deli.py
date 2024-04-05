sandwich_orders = ['tuna', 'turkey', 'roast beef', 'rueben', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"I have made the {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print(f"The following sandwiches have been completed:\n")
print(finished_sandwiches)
