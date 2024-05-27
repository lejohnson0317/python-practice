from pathlib import Path
import json

def greet_user():
    """Looks up a user in the verify_username.json file.
    Welcomes them if they are a returning user."""

    username = input("What is your username? ")

    path = Path('verify_user.json')
    path_exists = path.exists()
    if path_exists == True:
        contents = path.read_text()
        user_info = json.loads(contents)
        #print(user_info)
        #print(user_info['username'])
        if username == user_info['username']:
            full_name = user_info['full_Name'] 
            print(f"Welcome back, {full_name.title()}!")
            print(f"Below is your user information.\n{contents}")
        else:
            create_user_json(username)

def create_user_json(username):
    path = Path('verify_user.json')
    print("I don't recognize this username.  Let's add you to the list.")
    user_info = {}
    user_info['username'] = username
    user_info['full_Name'] = input("what's your full name? ")
    user_info['email'] = input("What's your email address? ")
    contents = json.dumps(user_info)
    path.write_text(contents)

    print(f"Thanks for providing your information.")
    print(f"You entered the following information:\n{contents}")

greet_user()
