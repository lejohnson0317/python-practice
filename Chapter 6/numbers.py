favorite_numbers = {
    'Dad': [16, 46],
    'Rod': [22, 25, 67],
    'Shellie': [25, 13, 69],
    'Garrett': [25, 4, 500],
    'Carter': [13, 5, 243]
    }

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for num in numbers:
        print(f"\t{num}")