# File name: Exercise7.6.py
# Author: Yolanda Theodorakis
# Description: Still practicing the use of dictionary. Implement a simple quiz 
#              where the user is asked the capitals of countries. First, make 
#              a text file with at least 50 countries with their capitals. The 
#              information is read at the beginning of the program into the 
#              dictionary. In the quiz itself, the user is asked the capitals 
#              of ten countries. When correctly answered by the user, proceed 
#              to the next question. If the user answers incorrectly, they 
#              will be shown the correct answer and then proceed to the next 
#              question. After ten questions, the user is informed of the 
#              number of correct answers.

import random

# Variable for the file path
countries = 'C:/Users/Yolanda/Desktop/ObjectOrientedProgramming/Object_Oriented_Programming/Exercise7/countries.txt'

# Empty dictionary
dictionary = {}

# Read the lines from the file and store them in the dictionary
with open(countries) as country_list:
    for line in country_list:
        (key, val) = line.split()
        dictionary[key] = val

def capital_quiz():
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
        
capital_quiz()
