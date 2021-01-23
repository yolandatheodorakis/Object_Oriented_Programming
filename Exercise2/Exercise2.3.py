# File name: Exercise2.3.py
# Author: Yolanda Theodorakis
# Description: Code task 2. Program asks for user to input the number of 
#              accepted exercises and prints out the grade. Simple code is 
#              enough, no objects needed. 

def get_grade ():
    # Asks for user input and changes that to integer
    exercises = int(input('How many accepted exercises? '))

    # Checks the number of exercises and prints the correct grade
    if exercises < 9:
        print('Grade is 0')

    elif exercises == 9:
        print('Grade is 1')
    
    elif exercises == 10:
        print('Grade is 2')

    elif exercises == 11:
        print('Grade is 3')

    elif exercises == 12:
        print('Grade is 4')

    elif exercises == 13:
        print('Grade is 5')

get_grade()
