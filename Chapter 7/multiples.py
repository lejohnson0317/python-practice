number = input("Give me an number and I will tell you if it's a multiple of 10: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is a multiple of 10")
else:
    print(f"{number} is not a multipe of 10")