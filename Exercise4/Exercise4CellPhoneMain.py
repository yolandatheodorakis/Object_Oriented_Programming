# File name: Exercise4CellPhoneMain.py
# Author: Yolanda Theodorakis
# Description: Take the Cell phone class of last week and divide the cell 
#              phone class into another file. Leave the main function in the 
#              original file. Test that your code still works.
#              Add and ID data attribute (integer between 1-6) to the cell 
#              phone. Cell phone class shall have accessor and mutator methods 
#              for all data attributes. Also check the __str__ method is up 
#              to date.

import Exercise4CellPhoneClass as phone

def main ():
    # Create new object from CellPhone class
    cell_phone = phone.CellPhone()

    # Ask for user to input manufacturer, model, retail price and id
    cell_phone.set_manufact()
    cell_phone.set_model()
    cell_phone.set_retail_price()
    cell_phone.set_id()

    # Print the data
    print('Here is the data that you provided:')
    print(cell_phone)


main()
