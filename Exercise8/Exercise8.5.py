# File  name: Exercise8.5.py
# Author: Yolanda Theodorakis
# Description: Continue with the “Countries and Capitals” quiz. Give the user 
#              a chance to test his/her knowledge with countries based on 
#              capitals.

import random

# Variable for the file path
countries_capitals = 'C:/Users/Yolanda/Desktop/ObjectOrientedProgramming/Object_Oriented_Programming/Exercise8/countries.txt'

def capital_quiz():
    # Empty dictionary
    dictionary = {}

    # Read the lines from the file and store them in the dictionary
    with open(countries_capitals) as country_list:
        for line in country_list:
            (key, val) = line.split()
            dictionary[key] = val

    # Variable for right answers
    right = 0

    countries = list(dictionary.keys())

    # Ask 10 capitals from user
    for i in range(1, 11):
        print('Question ' + str(i))
        country = random.choice(countries)
        capital = dictionary[country]
        user_guess = input('What is the capital of %s? '%country )

        # If user guesses right, add one point
        # If wrong, print the correct answer
        if user_guess.title() == capital:
            right += 1
        else:
            print('Incorrect. The capital of {} is {}.'.format(country, capital))

    # Print the total points
    print('You scored ' + str(right) + '/10 points.')
        

def country_quiz():
    # Empty dictionary
    dictionary = {}

    # Read the lines from the file and store them in the dictionary
    with open(countries_capitals) as country_list:
        for line in country_list:
            (val, key) = line.split()
            dictionary[key] = val

    # Variable for right answers
    right = 0

    capitals = list(dictionary.keys())

    # Ask 10 countries from user
    for i in range(1, 11):
        print('Question ' + str(i))
        capital = random.choice(capitals)
        country = dictionary[capital]
        user_guess = input('%s is the capital of? '%capital )

        # If user guesses right, add one point
        # If wrong, print the correct answer
        if user_guess.title() == country:
            right += 1
        else:
            print('Incorrect. {} is the capital of {}.'.format(capital, country))

    # Print the total points
    print('You scored ' + str(right) + '/10 points.')


def main():
    while True:
        # Ask which quiz user wants to play
        print('Do you want to test your knowledge on countries or capitals?')
        user_choice = input('Write "countries" or "capitals": ')

        if user_choice == 'countries':
            country_quiz()
        elif user_choice == 'capitals':
            capital_quiz()

        # Ask if user wants to continue playing
        yes_no = input('Do you want to continue playing? ')
        if (yes_no == 'yes') or (yes_no == 'Yes'):
            continue
        elif (yes_no == 'no') or (yes_no == 'No'):
            break


main()
