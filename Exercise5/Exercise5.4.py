# File name: Exercise5.4.py
# Author: Yolanda Theodorakis
# Description: Create multiple dices (at least three) and put them in a list. 
#              See that your dice can be rolled and the side can be shown. 
#              Create a small game where the best sum of three rolls wins. If 
#              the sum is a tie, tied dices are rolled as long as a winner is 
#              found (best side wins). Use functions and pass objects (or list 
#              of objects) as arguments. Use informative and clear output prints.

import random 

class Dice:
    # Initializes the state for the dice's number
    def __init__ (self):
        self.number = 0
        self.id = 0

    # Simulates the roll of a dice
    def roll (self):
        self.number = random.randint(1, 6)

    # Returns the dice number
    def get_number (self):
        return self.number

    # Set an dget id
    def set_id (self, dice_id):
        self.id = dice_id

    def get_id (self):
        return self.id

# Creates three dices and puts them in a list
def make_list ():
    # Create an empty list
    dice_list = []

    for number in range(1, 4):
        my_dice = Dice()
        my_dice.set_id(number)

        # Put the create dices in the list
        dice_list.append(my_dice)

    # Return the list
    return dice_list

# Rolls dices three times and puts the sums in a list
def roll_dices (dice_list):
    sum_list = []
    for item in dice_list:
        sum_of_rolls = 0
        for number in range(1, 4):
            item.roll()
            print('Dice', item.get_id(), 'roll', number, '->', item.get_number())
            sum_of_rolls += item.get_number()
        sum_list.append(sum_of_rolls)    

    return sum_list

def main ():
    # Create the list of dices
    dices = make_list()

    # Roll the dices and save the sum in a variable
    sum_list = roll_dices(dices)

    # Find the inde x of max value
    winner = sum_list.index(max(sum_list))
    
    if winner == 0:
        print('Dice 1 wins!')
    elif winner == 1:
        print('Dice 2 wins!')
    elif winner == 2:
        print('Dice 3 wins!')


main()
