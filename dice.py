from random import randint

class Dice:
    """Randomly rolls dice"""
    def __init__(self, sides=0):
        self.sides = sides

    def roll_d4(self, sides=4):
        print(randint(1, 4))

    def roll_d6(self, sides=6):
        print(randint(1, 6))
    
    def roll_d8(self, sides=8):
        print(randint(1, 6))
    
    def roll_d10(self, sides=10):
        print(randint(1, 10))
    
    def roll_d12(self, sides=12):
        print(randint(1, 12))
    
    def roll_d20(self, sides=20):
        print(randint(1, 20))
    
    def roll_d100(self, sides=100):
        print(randint(1, 100))