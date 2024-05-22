from pathlib import Path

guest_input = input("Please enter your name: ").title()

path = Path('guest.txt')
path.write_text(guest_input)