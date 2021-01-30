# File name: Exercise3.6.py
# Author: Yolanda Theodorakis
# Description: Create two Dice objects and roll them both. Sum the result 
#              and print to screen.

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


def main ():
    # Create two objects from Dice class
    my_dice = Dice()
    your_dice = Dice()

    # Roll the dice and generate
    print('I am rolling the dice ...')
    my_dice.roll()
    your_dice.roll()

    # Save the dice numbers into variables
    my_number = my_dice.get_number()
    your_number = your_dice.get_number()
    sum_of_numbers = my_number + your_number

    # Print the sum
    print('The sum is ', sum_of_numbers)
    

main()
