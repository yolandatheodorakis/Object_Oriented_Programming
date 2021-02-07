# File name: Exercise4CellPhoneClass.py
# Author: Yolanda Theodorakis
# Description: Take the Cell phone class of last week and divide the cell 
#              phone class into another file. Leave the main function in the 
#              original file. Test that your code still works.

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

    # Print the state
    def __str__ (self):
        return ('Manufacturer: ' + format(self.manufact) +
                '\nModel numeber: ' + format(self.model) + 
                '\nRetail price: ' + format(self.retail_price))
