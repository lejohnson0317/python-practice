favorite_places = {
    'shellie': ['gulf shores', 'hawaii', 'caribbean'],
    'larry': ['germany', 'arkansas', 'hawaii'],
    'carter': ['texas']
    }

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")