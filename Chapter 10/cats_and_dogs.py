from pathlib import Path

paths = ['cats.txt', 'dogs.txt']

for path in paths:
    path = Path(path) 
    try:
        contents = path.read_text()
    except FileNotFoundError:
        #print(f"Sorry, the file {path} does not exist.")
        pass
    else:
        print(contents.title())