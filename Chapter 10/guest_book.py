from pathlib import Path

prompt = "Please enter your name for our guest book: "
prompt += "\nEnter 'quit' when you are finished. "

guest_book = ""
active = True
while active:
    guest_input = input(prompt).title()

    if guest_input != 'Quit':
        guest_book += guest_input + "\n"
    else:
        active = False
        print("Thank you for your participation!")

path = Path('guest_book.txt')
path.write_text(guest_book)