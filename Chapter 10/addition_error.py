print("I can add two numbers for you.\n")

try:
    number1 = int(input("  Enter a number: "))
    number2 = int(input("  Enter another number: "))
except ValueError:
    print("Sorry, you did not enter a number. Try again.")
    quit()
else:
    addition = number1 + number2
    print(addition)