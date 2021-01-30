# File name: Exercise3.8.py
# Author: Yolanda Theodorakis
# Description: Create a CellPhone class. Write a program that will design a 
#              class that represents a cell phone. The data attributes are 
#              manufact, model, and retail_price. The class will also have 
#              following methods: __init__, set_manufact, set_model, 
#              set_retail_price, get_manufact, get_model, get_retail_price. 
#              Test your CellPhone Class by writing a main function that 
#              creates the needed objects and prompts the user for the phone's 
#              manufacturer, model and retail price.

class CellPhone:
    # Initialize the states for manufacturer, model and retail price
    def __init__ (self):
        self.manufact = ''
        self.model = ''
        self.retail_price = ''

    # Set the manufacturer from user input
    def set_manufact (self):
        self.manufact = input('Enter the manufacturer: ')

    # Set the model from user input
    def set_model (self):
        self.model = input('Enter the model number: ')

    # Set the retail price from user input
    def set_retail_price (self):
        self.retail_price = input('Enter the retail price: ')
    
    # Return the manufacturer
    def get_manufact (self):
        return self.manufact

    # Return the model
    def get_model (self):
        return self.model

    # Return the retail price
    def get_retail_price (self):
        return self.retail_price


def main ():
    # Create new object from CellPhone class
    cell_phone = CellPhone()

    # Ask for user to input manufacturer, model and retail price
    cell_phone.set_manufact()
    cell_phone.set_model()
    cell_phone.set_retail_price()

    # Print the data
    print('Here is the data that you provided:')
    print('Manufacturer:', cell_phone.get_manufact())
    print('Model number:', cell_phone.get_model())
    print('Retail price:', cell_phone.get_retail_price())


main()
