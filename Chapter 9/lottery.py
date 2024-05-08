from random import randint
x = 0
lottery_drawing = []

lottery_choices = (3, 16, 42, 8, 19, 47, 38, 5, 26, 33, 'g', 'e', 'p', 'z', 't')

while x < 4:
    choice = randint(0, 14)
    draw = lottery_choices[choice]
    lottery_drawing.append(draw)
    x += 1
print("If you have the following 4 numbers or letters, you have won the lottery!")
print(lottery_drawing)