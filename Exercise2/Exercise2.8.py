# File name: Exercise2.8.py
# Author: Yolanda Theodorakis
# Description: Modify the toss_the_coin() function so that there are 2 more 
#              options: Coin lands on the table upright (and not flat showing 
#              heads or tails) or coin drops on the ground and disappears (on 
#              a rabbit hole). Name the options properly and give informative 
#              and readable output of the status.

import random

class Coin:

    # The __init__ method initializes the sideup data attribute with 'Heads'
    def __init__ (self):
        self.sideup = 'Heads'

    # The toss method generates a random number in the range of 0 through 3 
    # and changes the sideup
    def toss (self):
        if random.randint(0, 3)  == 0:
            self.sideup = 'Heads'

        elif random.randint(0, 3)  == 1:
            self.sideup = 'Tails'

        elif random.randint(0, 3)  == 2:
            self.sideup = 'upright'

        elif random.randint(0, 3)  == 3:
            self.sideup = 'disappeared'

    # The get_sideup method returns the value referenced by sideup
    def get_sideup (self):
        return self.sideup


# The main function
def main ():

    # Create an object from the Coin class
    my_coin = Coin()

    # Display the side of the coin that is facing up
    print('This side is up: ', my_coin.get_sideup())

    # Toss the coin
    print('I am tossing the coin ...')
    my_coin.toss()

    # Display the side of the coin that is now facing up
    if my_coin.get_sideup() == 'Heads':
        print('The Heads side is up')
    elif my_coin.get_sideup() == 'Tails':
        print('The Tails side is up')
    elif my_coin.get_sideup() == 'upright':
        print('The coin stands upright')
    else:
        print('The coin disappeared')


main()
