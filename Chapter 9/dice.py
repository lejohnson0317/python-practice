from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        die_roll = randint(1, self.sides)
        return die_roll

roll1 = Die()   
print(roll1.roll_die ())
print(roll1.roll_die ())
print(roll1.roll_die ())
print(roll1.roll_die ())
print(roll1.roll_die ())

roll2 = Die(10)
print(roll2.roll_die ())
print(roll2.roll_die ())
print(roll2.roll_die ())
print(roll2.roll_die ())
print(roll2.roll_die ())

roll3 = Die(20)
print(roll3.roll_die ())
print(roll3.roll_die ())
print(roll3.roll_die ())
print(roll3.roll_die ())
print(roll3.roll_die ())