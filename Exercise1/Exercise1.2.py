# File name: Exercise1.2.py
# Author: Yolanda Theodorakis
# Description: Code a list of at least 10 items and fill it with numbers asked 
#              from user. Do the same with strings. Print out both lists. Then 
#              fill the number list with randomly generated numbers and print 
#              it out.

# Ask ten numbers from user and put them in a list
numbers = [input('Submit a number: ') for i in range(10)]

# Ask ten strings from user and put them in a list
strings = [input('Submit a string: ') for i in range(10)]

# Print both lists
print(numbers)
print(strings)

# Fill number list with random numbers and print them
import random

numbers.clear()
numbers = random.sample(range(100), 10)
print(numbers)
