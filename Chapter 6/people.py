person_0 = {
    'first_name': 'Larry',
    'last_name': 'Johnson',
    'age': 56,
    'city': "Grapevine",
    }
person_1 = {
    'first_name': 'George',
    'last_name': 'Schwing',
    'age': 57,
    'city': "Covington",
    }
person_2 = {
    'first_name': 'Jim',
    'last_name': 'Thomson',
    'age': 45,
    'city': "Dallas",
    }

people = [person_0, person_1, person_2]

for person in people:
        user = f"{person['first_name']} {person['last_name']}"
        print(f"{user.title()} is {person['age']} and lives in {person['city'].title()}.")
