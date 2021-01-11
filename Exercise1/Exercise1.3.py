# File name: Exercise1.3.py
# Author: Yolanda Theodorakis
# Description: Arrange numbers in the list from smallest to largest and 
#              strings in alphabetical order and print out the lists.

# Number and string lists
numbers = [6, 90, 12, 83, 100, 22, 75, 8, 33, 60]
strings = ['hello', 'banana', 'lamp', 'computer', 'mouse', 'phone', 
           'code', 'glass', 'pen', 'ring']

# Numbers from smallest to largest
numbers.sort()

# Strings in alphabetical order
strings.sort()

# Print both lists
print(numbers)
print(strings)
