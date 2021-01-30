# File name: Exercise3.5.py
# Author: Yolanda Theodorakis
# Description: Create a class Dice and make an object of it. You shall be able 
#              to roll the dice, get the result (number between 1-6) and get 
#              its colour. Add at least 1 extra feature. Design your program 
#              using pseudocode. Document your code properly (with good 
#              comments) and pay attention to the clarity of the output prints.

import random

class Dice:
    # Initializes the states for the dice's number, colour 
    # and my favourite combo
    def __init__ (self):
        self.number = 1
        self.colour = 'blue'
        self.fav_combo = 'NO'

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

    # Generates the colour
    def set_colour (self):
        if random.randint(0, 5) == 0:
            self.colour = 'blue'
        elif random.randint(0, 5) == 1:
            self.colour = 'yellow'
        elif random.randint(0, 5) == 2:
            self.colour = 'pink'
        elif random.randint(0, 5) == 3:
            self.colour = 'red'
        elif random.randint(0, 5) == 4:
            self.colour = 'white'
        elif random.randint(0, 5) == 5:
            self.colour = 'black'

    # Check if it's my favourite combo
    def set_fav_combo (self):
        if (self.number == 3 and self.colour == 'pink'):
            self.fav_combo = 'YES'
        else: self.fav_combo = 'NO'

    # Returns the dice number
    def get_number (self):
        return self.number

    # Returns the dice colour
    def get_colour (self):
        return self.colour

    # Returns yes if it's my favourite combo, else no
    def get_fav_combo (self):
        return self.fav_combo


def main ():
    # Create an object from Dice class
    my_dice = Dice()

    # Roll the dice and generate the colour
    print('I am rolling the dice ...')
    my_dice.roll()
    my_dice.set_colour()

    # Get the dice number and colour and if it's my favourite combo
    print('The dice number is', my_dice.get_number(), 
        'and the colour is', my_dice.get_colour())
    print('Is it my favourite combo?', my_dice.get_fav_combo())


main()

# Pseudocode #
#
#   class Dice:
#       initialize states:
#           number = 1
#           colour = blue
#           fav_combo = no

#       function roll:
#           if random number = 0:
#               number = 1
#           elif random number = 1:
#               number = 2
#           elif random number = 2:
#               number = 3
#           elif random number = 3:
#               number = 4
#           elif random number = 4:
#               number = 5
#           elif random number = 5:
#               number = 6

#       function set_colour:
#           if random number = 0:
#               colour = blue
#           elif random number = 1:
#               colour = yellow
#           elif random number = 2:
#               colour = pink
#           elif random number = 3:
#               colour = red
#           elif random number = 4:
#               colour = white
#           elif random number = 5:
#               colour = black

#       function set_fav_combo:
#           if number = 3 and colour = pink:
#               fav_combo = yes
#           else: fav_combo = no
#
#       function get_number:
#           return number

#        function get_colour:
#            return colour

#        function get_fav_combo:
#            return fav_combo

#   main function:
#       my_dice = new object from Dice

#        print 'I am rolling the dice ...'
#        roll the dice
#        set the colour

#        print 'The dice number is', get_number, 
#            'and the colour is', get_colour
#        print 'Is it my favourite combo?', get_fav_combo