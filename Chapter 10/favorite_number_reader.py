from pathlib import Path
import json

path = Path('favorite_number.json')
favorite_number = json.loads(path.read_text())
print(f"You favorite number is {favorite_number}!")