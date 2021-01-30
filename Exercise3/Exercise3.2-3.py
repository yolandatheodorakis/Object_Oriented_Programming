# File name: Exercise3.2-3.py
# Author: Yolanda Theodorakis
# Description: Modify the Coin class so that in addition to sideup you have 
#              another data attribute called currency. Add a function 
#              generating the currency (Euro, Pound, Dollar, Ruble, Yen). 
#              Use a random generator to get the currency. Add a function to 
#              print out the currency.
#              Add a method that can change the currency of the coin.

import random

class Coin:

    # The __init__ method initializes the sideup data attribute with 'Heads'
    # and the currency data attribute with 'Euro'
    def __init__ (self):
        self.sideup = 'Heads'
        self.currency = 'Euro'

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

    # The currency method generates a random number in the range of 0 through 4 
    # and returns a different currency
    def generate_currency (self):
        if random.randint(0, 4) == 0:
            return 'Euro'
        elif random.randint(0, 4) == 1:
            return 'Pound'
        elif random.randint(0, 4) == 2:
            return 'Dollar'
        elif random.randint(0, 4) == 3:
            return 'Ruble'
        elif random.randint(0, 4) == 4:
            return 'Yen'

    # The set_currency changes the currency
    def set_currency (self):
        self.currency = self.generate_currency()

    # The get_sideup method returns the value referenced by sideup
    def get_sideup (self):
        return self.sideup

    # The get_currency method returns the value referenced by currency
    def get_currency (self):
        return self.currency


# The main function
def main ():

    # Create an object from the Coin class
    my_coin = Coin()

    # Display the side of the coin that is facing up and the current currency
    print('This side is up:', my_coin.get_sideup(), 
        'and the currency is', my_coin.get_currency())

    # Toss the coin
    print('I am tossing the coin ...')
    my_coin.toss()

    # Generate the currency
    print('I am generating the currency ...')
    my_coin.set_currency()

    # Display the side of the coin that is now facing up
    if my_coin.get_sideup() == 'Heads':
        print('The Heads side is up')
    elif my_coin.get_sideup() == 'Tails':
        print('The Tails side is up')
    elif my_coin.get_sideup() == 'upright':
        print('The coin stands upright')
    else:
        print('The coin disappeared')

    # Display the currency
    if my_coin.get_currency() == 'Euro':
        print('and the currency is Euro')
    elif my_coin.get_currency() == 'Pound':
        print('and the currency is Pound')
    elif my_coin.get_currency() == 'Dollar':
        print('and the currency is Dollar')
    elif my_coin.get_currency() == 'Ruble':
        print('and the currency is Ruble')
    elif my_coin.get_currency() == 'Yen':
        print('and the currency is Yen')


main()
