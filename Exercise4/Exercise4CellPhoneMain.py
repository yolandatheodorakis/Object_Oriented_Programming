# File name: Exercise4CellPhoneMain.py
# Author: Yolanda Theodorakis
# Description: Create different cell phone objects (which have different data 
#              attribute values, use mutator methods to change the data 
#              attribute values). Print out each object’s state (use the 
#              __str__ method in the cell phone class).

import Exercise4CellPhoneClass as phone

def main ():
    # Create new objects from CellPhone class
    cell_phone_1 = phone.CellPhone()
    cell_phone_2 = phone.CellPhone()
    cell_phone_3 = phone.CellPhone()
    cell_phone_4 = phone.CellPhone()
    cell_phone_5 = phone.CellPhone()
    cell_phone_6 = phone.CellPhone()

    # Ask for user to input manufacturer, model, retail price and id
    cell_phone_1.set_manufact()
    cell_phone_1.set_model()
    cell_phone_1.set_retail_price()
    cell_phone_1.set_id()

    cell_phone_2.set_manufact()
    cell_phone_2.set_model()
    cell_phone_2.set_retail_price()
    cell_phone_2.set_id()

    cell_phone_3.set_manufact()
    cell_phone_3.set_model()
    cell_phone_3.set_retail_price()
    cell_phone_3.set_id()

    cell_phone_4.set_manufact()
    cell_phone_4.set_model()
    cell_phone_4.set_retail_price()
    cell_phone_4.set_id()

    cell_phone_5.set_manufact()
    cell_phone_5.set_model()
    cell_phone_5.set_retail_price()
    cell_phone_5.set_id()

    cell_phone_6.set_manufact()
    cell_phone_6.set_model()
    cell_phone_6.set_retail_price()
    cell_phone_6.set_id()

    # Print the data
    print('Here is the data that you provided:')
    print(cell_phone_1)

    print('Here is the data that you provided:')
    print(cell_phone_2)

    print('Here is the data that you provided:')
    print(cell_phone_3)

    print('Here is the data that you provided:')
    print(cell_phone_4)

    print('Here is the data that you provided:')
    print(cell_phone_5)

    print('Here is the data that you provided:')
    print(cell_phone_6)

    
main()
