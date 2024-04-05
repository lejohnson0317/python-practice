vacation = {}
polling_active = True

while polling_active:
    name = input("What is your name? ")
    place = input ("What is your dream vacation? ")

    vacation[name] = place

    repeat = input("Would you like anyone else to respond? (yes/no) \n").lower()
    if repeat == 'no':
        polling_active = False
    
for name, place in vacation.items():
    print(f"{name} wants to go to {place}.")

