from pathlib import Path
import json

path = Path('favorite_number.json')
favorite_number = input("What's your favorite number? ")
contents = json.dumps(favorite_number)
path.write_text(contents)