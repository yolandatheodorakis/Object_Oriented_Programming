# File name: Exercise4CellPhoneMain.py
# Author: Yolanda Theodorakis
# Description: Take the Cell phone class of last week and divide the cell 
#              phone class into another file. Leave the main function in the 
#              original file. Test that your code still works.

import Exercise4CellPhoneClass as phone

def main ():
    # Create new object from CellPhone class
    cell_phone = phone.CellPhone()

    # Ask for user to input manufacturer, model and retail price
    cell_phone.set_manufact()
    cell_phone.set_model()
    cell_phone.set_retail_price()

    # Print the data
    print('Here is the data that you provided:')
    print(cell_phone)


main()
