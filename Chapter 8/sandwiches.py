def build_sandwich(*ingredients):
    """We are going to build  a sandwich with the ingredients listed"""
    print(f"Your sandwich will be made with the following ingredients:\n")
    for ingredient in ingredients:
        print(f"- {ingredient}")

build_sandwich('Mayo', 'lettuce', 'tomato', 'turkey')
build_sandwich('mustard', 'pastrami', 'sourkraut', 'dressing', 'pickles')
build_sandwich('mayo', 'ham', 'cheese')