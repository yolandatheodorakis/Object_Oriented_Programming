# File name: Exercise2.5.py
# Author: Yolanda Theodorakis
# Description: Code task 4. Program accepts student's name and grade as input 
#              and counts the average of grades of all students. Simple code 
#              is enough, no objects needed.

def count_average ():
    # Variable for the number of students so the loop stops at the right time
    number_of_students = 0

    # The sum of all grades
    sum_of_grades = 0

    while number_of_students < 5:
        # Asks the user to input a name and a grade
        input('Input the name of student: ')
        grade = int(input('Input the grade: '))

        # Increase the number of students
        number_of_students += 1

        # Add the grade to the sum
        sum_of_grades += grade

        # Counts the average
        average = sum_of_grades / number_of_students

    print('The average of the grades is ', average)

count_average()
