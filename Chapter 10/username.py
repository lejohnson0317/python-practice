from pathlib import Path
import json

def get_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
 
def greet_user():
    """Greet user by name"""
    path = Path('username.json')
    username = get_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

def get_new_username(path):
    """Get new username if path does not exist"""
    username = input("What's your name? ")
    path = Path('username.json')
    contents = json.dumps(username)
    path.write_text(contents)
    return username

greet_user()
