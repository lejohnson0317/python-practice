print("I can add two numbers for you.")
print("Enter 'q' at any time to quit.\n")

def add_two_numbers(number1, number2):
    addition = number1 + number2
    print(f"{number1} + {number2} = {addition}")

active = True

while active:
    try:
        number1 = input("  Enter a number: ")
        if number1 == 'q':
            break
        number1 = int(number1)

        number2 = input("  Enter another number: ")  
        if number2 == 'q':
            break
        number2 = int(number2)

        add_two_numbers(number1, number2) 
    except ValueError:
        print("Sorry, you did not enter a number. Try again.")
