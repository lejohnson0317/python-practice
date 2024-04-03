pets = []

pet = {
    "owner": "alice",
    "type": "cat",
    "breed": "siamese",
    }

pets.append(pet)

pet = {
    "owner": "bob",
    "type": "dog",
    "breed": "golden retriever",
    }

pets.append(pet)

pet = {
    "owner": "kim",
    "type": "snake",
    "breed": "boa constrictor",
    }

pets.append(pet)

pet = {
    "owner": "tina",
    "type": "cat",
    "breed": "maine Coon",
    }

pets.append(pet)

pet = {
    "owner": "lisa",
    "type": "dog",
    "breed": "border collie"
    }

pets.append(pet)

for pet in pets:
    print(f"{pet['owner'].title()} has a {pet['type']} and its breed is {pet['breed'].title()}.")    