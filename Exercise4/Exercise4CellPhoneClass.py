# File name: Exercise4CellPhoneClass.py
# Author: Yolanda Theodorakis
# Description: Take the Cell phone class of last week and divide the cell 
#              phone class into another file. Leave the main function in the 
#              original file. Test that your code still works.
#              Add and ID data attribute (integer between 1-6) to the cell 
#              phone. Cell phone class shall have accessor and mutator methods 
#              for all data attributes. Also check the __str__ method is up 
#              to date.

class CellPhone:
    # Initialize the states for manufacturer, model, retail price and id
    def __init__ (self):
        self.manufact = ''
        self.model = ''
        self.retail_price = ''
        self.id = 1

    # Set the manufacturer from user input
    def set_manufact (self):
        self.manufact = input('Enter the manufacturer: ')

    # Set the model from user input
    def set_model (self):
        self.model = input('Enter the model number: ')

    # Set the retail price from user input
    def set_retail_price (self):
        self.retail_price = input('Enter the retail price: ')

    # Set the id from user input
    def set_id (self):
        self.id = input('Enter the id: ')
    
    # Return the manufacturer
    def get_manufact (self):
        return self.manufact

    # Return the model
    def get_model (self):
        return self.model

    # Return the retail price
    def get_retail_price (self):
        return self.retail_price

    # Return the id
    def get_id (self):
        return self.id

    # Print the state
    def __str__ (self):
        return ('Manufacturer: ' + format(self.manufact) +
                '\nModel numeber: ' + format(self.model) + 
                '\nRetail price: ' + format(self.retail_price) + 
                '\nID: ' + format(self.id))
