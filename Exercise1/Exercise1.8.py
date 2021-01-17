# File name: Exercise1.8.py
# Author: Yolanda Theodorakis
# Description: Code a simple (and textual) implementation of 
#              Rock-Paper-Scissors game. Best of 3 games wins. Plan your game 
#              first and code piece by piece: read input from user, generate 
#              random number to get computer’s choice, then check who wins and 
#              keep track of victories. Use functions.

import random

def rock_paper_scissors ():

    game_number = 1 # Increases every round so the game stops after 3 rounds
    user_choice = None # User's choice
    computer_choice = random.randint(1, 3) # Computer's random choice

    user_wins = 0
    computer_wins = 0

    while game_number < 4:

        game_number += 1
        user_choice = int(input("1 -> rock, 2 -> paper, 3 -> scissors: "))
        print("Computer's choice: ", computer_choice)

        # Checks if user won
        if ((user_choice == 1 and computer_choice == 3) or 
              (user_choice == 2 and computer_choice == 1) or 
              (user_choice == 3 and computer_choice == 2)):
              print("One point for user.")
              user_wins += 1

        # If it's a tie the loop continues
        elif user_choice == computer_choice:
            continue
        
        # Point for computer if it won
        else:
            print("One point for computer.")
            computer_wins += 1

    # Checks the number of wins and prints out who won
    if user_wins == computer_wins:
        print("It's a tie.")
    elif user_wins > computer_wins:
        print("User wins.")
    else:
        print("Computer wins.")

rock_paper_scissors()
