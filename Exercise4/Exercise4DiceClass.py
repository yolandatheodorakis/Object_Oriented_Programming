# File name: Exercise4DiceClass.py
# Author: Yolanda Theodorakis
# Description: Take the Dice class from your earlier exercises and place that 
#              to its own file. Then in main function roll a dice and based on 
#              the result choose the correct cell phone based on the ID. Print 
#              out the chosen cell phone object’s state.

import random

class Dice:
    # Initializes the state for the dice's number
    def __init__ (self):
        self.number = 1

    # Simulates the roll of a dice
    def roll (self):
        if random.randint(0, 5) == 0:
            self.number = 1
        elif random.randint(0, 5) == 1:
            self.number = 2
        elif random.randint(0, 5) == 2:
            self.number = 3
        elif random.randint(0, 5) == 3:
            self.number = 4
        elif random.randint(0, 5) == 4:
            self.number = 5
        elif random.randint(0, 5) == 5:
            self.number = 6

    # Returns the dice number
    def get_number (self):
        return self.number
