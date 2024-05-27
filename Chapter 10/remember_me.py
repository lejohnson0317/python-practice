from pathlib import Path
import json

user_info = {}

user_info['username'] = input("What's your user name? ")
user_info['full_Name'] = input("what's your full name? ")
user_info['email'] = input("What's your email address? ")

#print(user_info)

path = Path('username.json')
contents = json.dumps(user_info)
path.write_text(contents)

print(f"Thanks for providing your information.")

path = Path('username.json')
contents = json.loads(path.read_text())
print(f"Please make sure the following is correct:\n{contents}!")

