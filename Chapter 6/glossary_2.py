prog_words = {
    'variable': "where a value can be stored.",
    'title': "how to capitalize the first letter of every word in a sentence.",
    'list': "a collection of items within a single variable.",
    'function': "a block of code that performs a specific task.",
    'loop': "a control structure used for repeating an action",
    }


for key, variable in sorted(prog_words.items()):
    print(f"\n{key.title()}: {variable}")