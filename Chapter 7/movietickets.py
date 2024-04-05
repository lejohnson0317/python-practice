prompt = "Please enter the movie goer's age. Enter 'q' to quit: "

age = ""

while True:
    age = input(prompt)
    if age == 'q':
        break

    age = int(age)
    
    if age <= 3:
        print("Your ticket is free!")
    elif age >= 4 and age <= 13:
        print("Your ticket costs $10.")
    else:
        print("Your ticket price is $15.")