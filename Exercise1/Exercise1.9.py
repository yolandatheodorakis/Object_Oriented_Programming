# File name: Exercise1.9.py
# Author: Yolanda Theodorakis
# Description: Code a function that returns a random number between 1-6 when 
#              calling it. Print out the number where the function is called 
#              (so do not print the number inside the function).

import random

def random_number ():
    # Generate a random number
    number = random.randint(1, 6)

    # Return that number
    return number

# Call the function inside the print
print(random_number())
