rivers = {
    'mississippi': 'usa',
    'nile': 'egypt',
    'amazon': 'brazil',
}

for river, country in rivers.items():
    print(f"\nThe {river.title()} runs through {country.title()}.")

for river in sorted(rivers.keys()):
    print(f"{river.title()}")

for country in sorted(rivers.values()):
    print(f"{country.title()}")