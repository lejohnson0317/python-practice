from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
print(contents)

for line in contents.splitlines():
    python_list = ""
    python_list += line.replace("Python", "C")
    print(python_list)