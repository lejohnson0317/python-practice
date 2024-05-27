from pathlib import Path
import json

def get_favorite_number(path):
    """Checks for file favorite_number.json and returns the favorite number."""
    if path.exists():
        favorite_number = json.loads(path.read_text())
        return favorite_number
    
def input_favorite_number(path):
    """Writes the favorite number to a file."""
    
    favorite_number = input("What's your favorite number? ")
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    return favorite_number

def reveal_favorite_number():
    """Shows the uer their favorite number."""

    path = Path('favorite_number.json')
    favorite_number = get_favorite_number(path)
    if favorite_number:
        print(f"I know your favorite number! It's {favorite_number}!")
    else:
        favorite_number = input_favorite_number(path)
        print(f"I'll remember your favorite number, {favorite_number}, when you return!")


reveal_favorite_number()
