# File  name: Exercise8.3.py
# Author: Yolanda Theodorakis
# Description: Bake cookies

import random

class Cookie:
    def __init__(self):
        self.flavour = None
        self.frosted = False

    def set_flavour(self, flavour):
        self.flavour = flavour

    def get_flavour(self):
        return self.flavour

    def set_frosted(self):
        self.frosted = True

    def get_frosted(self):
        return self.frosted

    def __str__(self):
        if self.flavour == None:
            return ('The cookie is not frosted and it has no flavour.')
        else:
            return ('The cookie is frosted and the flavour is {}.'
                    .format(self.flavour))

                
def main():
    # List of possible frost flavours
    flavours = ['vanilla', 'chocolate', 'caramel', 'matcha', 'coffee']

    # Ask user their favourite flavour
    favourite_flavour = input('What is your favourite flavour? ')

    # Empty list for cookies
    cookies = []

    # Bake ten cookies
    print('Baking ten cookies...')
    for new_cookie in range(1, 10):
        new_cookie = Cookie()
        cookies.append(new_cookie)

    # Frost the cookies with random flavours
    print('Frosting the cookies...')
    for item in cookies:
        item.set_flavour(random.choice(flavours))
        item.set_frosted()

    # Get the amount of favourite flavour frosted cookies
    amount_of_favourites = 0
    for item in cookies:
        if item.get_flavour() == favourite_flavour:
            amount_of_favourites += 1

    # Check how many of the cookies are frosted with favourite flavour
    if amount_of_favourites > 0:
        print('You have {} cookie(s) that is/are frosted with \
               \nyour favourite flavor.'.format(amount_of_favourites))
    elif amount_of_favourites == 0:
        print('You need to bake more cookies if you want your favourite flavour.')


main()
