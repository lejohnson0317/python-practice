from pathlib import Path

def count_words(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        count = contents.lower().count('the ')
        print(f"The word 'the' appears {count} times in {path}.")
        
books = ['tarzan.txt', 'war_of_the_worlds.txt']

for book in books:
    path = Path(book)
    count_words(path)
    
