# File name: Exercise3.4.py
# Author: Yolanda Theodorakis
# Description: Change the Coin's sideup attribute to private. Test that your 
#              coin still works. What happens if you now try to change the 
#              attribute's value from the main function? Try it out!

import random

class Coin:

    # The __init__ method initializes the sideup data attribute with 'Heads'
    # and the currency data attribute with 'Euro'
    def __init__ (self):
        self.__sideup = 'Heads'
        self.currency = 'Euro'

    # The toss method generates a random number in the range of 0 through 3 
    # and changes the sideup
    def toss (self):
        if random.randint(0, 3)  == 0:
            self.__sideup = 'Heads'
        elif random.randint(0, 3)  == 1:
            self.__sideup = 'Tails'
        elif random.randint(0, 3)  == 2:
            self.__sideup = 'upright'
        elif random.randint(0, 3)  == 3:
            self.__sideup = 'disappeared'

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

    # the set_currency changes the currency
    def set_currency (self):
        self.currency = self.generate_currency()

    # The get_sideup method returns the value referenced by sideup
    def get_sideup (self):
        return self.__sideup

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

    # Try to change the sideup value, it doesn't change
    my_coin.__sideup = 'Tails'
    print(my_coin.get_sideup())


main()
