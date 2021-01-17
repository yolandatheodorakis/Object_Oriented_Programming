# File name: Exercise1.4-6.py
# Author: Yolanda Theodorakis
# Description: Write a program which repeatedly reads integers until the user 
#              enters 0. Print out the number of negative integers. Use 
#              functions in your solution. Add a function that counts the 
#              number of even integers that were among the entered. Add a 
#              function that counts the sum of the positive integers divisible 
#              by three.

def count_integers ():

    integer = None # This is compared to 0
    negatives = 0 # Negative integers
    evens = 0 # Even integers
    positive_and_divisible = 0 # Positive & divisible by three integrs


    # While the integer is not 0
    while integer != 0:
        # Asks for user input
        user_input = input("Submit an integer (0 terminates): ")

        # Changes that input to an integer and saves it into the variable
        integer = int(user_input)

        # Is integer negative & divisible by 2 = even
        if integer < 0 and integer % 2 == 0:
            negatives += 1
            evens += 1

        # Is integer negative
        elif integer < 0:
            negatives += 1 

        # Is integer positive & divisible by 3 & divisible by 2
        elif integer > 0 and integer % 3 == 0 and integer % 2 == 0:
            positive_and_divisible += 1
            evens += 1
        
        # Is integer divisible by 2 and not 0
        elif integer % 2 == 0 and integer != 0:
            evens += 1

        # Is integer positive & divisible by 3
        elif integer > 0 and integer % 3 == 0:
            positive_and_divisible += 1

        # Is integer other than 0
        elif integer != 0:
            continue # Continues the loop

        else:
            break # Breaks the loop

    # Prints the results
    print("Number of negative integers: ", negatives)
    print("Number of even integers: ", evens)
    print("Number of integers that are positive and divisible by three: ", 
        positive_and_divisible)

count_integers()
