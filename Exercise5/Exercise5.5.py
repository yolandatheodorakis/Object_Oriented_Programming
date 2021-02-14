# File name: Exercise5.5.py
# Author: Yolanda Theodorakis
# Description: Create a class called Player. Player has at least the following 
#              data attributes: first name, last name and a player id. 
#              Remember to code accessor and mutator methods and str-method. 
#              Create a dictionary so that the player id is a key and each 
#              player has one dice. Roll each player’s dice and print out each 
#              player’s dice’s side. Use informative and clear output print.

import random

class Player:
    # Initialize the states
    def __init__ (self):
        self.first_name = ''
        self.last_name = ''
        self.player_id = 0
        self.dice_number = 0

    # Set first name, last name and id
    def set_first_name (self):
        self.first_name = input('Enter first name: ')

    def set_last_name (self):
        self.last_name = input('Enter last name: ')

    def set_player_id (self, player_id):
        self.player_id = player_id

    # Simulates the roll of a dice
    def roll (self):
        self.dice_number = random.randint(1, 6)

    # Returns the dice number
    def get_dice_number (self):
        return self.dice_number

    # Get first name, last name and id
    def get_first_name (self):
        return self.first_name

    def get_last_name (self):
        return self.last_name

    def get_player_id (self):
        return self.player_id

    # Print the state
    def __str__ (self):
        return ("Player number " + format(self.player_id) + " is " + 
                 format(self.first_name) + " " + format(self.last_name) + 
                 " and their dice number is " + format(self.dice_number))

# This function creates the players and puts them in a list
def create_players ():
    players = []
    for number in range(1, 3):
        print("Enter the player", number,"'s information.")
        player = Player()
        player.set_first_name()
        player.set_last_name()
        player.set_player_id(number)
        players.append(player)
    return players

def get_choice ():
    print("\nChoose which player's dice you want to roll.")
    print('Press 1 for the first player.')
    print('Press 2 for the second player.')
    print('Press 0 to quit.')

    choice = int(input('Enter your choice: '))

    while choice < 0 or choice > 2:
        choice = int(input('Enter a valid choice: '))

    return choice

def main ():
    # Create players list
    print('First create the players.')
    players = create_players()

    # Initial value for choice
    choice = None    

    while choice != 0:
        choice = get_choice()

        # Based on user's choice roll the chosen player's dice
        # and print the state
        if choice == 1:
            players[0].roll()
            print(players[0])
        elif choice == 2:
            players[1].roll()
            print(players[1])


main()
