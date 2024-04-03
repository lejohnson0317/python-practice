seating = input("How many people are in your party? ")
seating = int(seating)

if seating > 8:
    print("You will have to wait for a table.")
else:
    print("We can seat you immediately!")