# File name: Exercise4CellPhoneMain.py
# Author: Yolanda Theodorakis
# Description: Create different cell phone objects (which have different data 
#              attribute values, use mutator methods to change the data 
#              attribute values). Print out each object’s state (use the 
#              __str__ method in the cell phone class).
#              Take the Dice class from your earlier exercises and place that 
#              to its own file. Then in main function roll a dice and based on 
#              the result choose the correct cell phone based on the ID. Print 
#              out the chosen cell phone object’s state.

import Exercise4CellPhoneClass as phone
import Exercise4DiceClass as dice

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

    # Create a dice object
    my_dice = dice.Dice()

    # Roll the dice
    my_dice.roll()

    # Print the chosen cell phone's state
    if my_dice.get_number() == 1:
        print('Here is the data that you provided:')
        print(cell_phone_1)
    elif my_dice.get_number() == 2:
        print('Here is the data that you provided:')
        print(cell_phone_2)
    elif my_dice.get_number() == 3:
        print('Here is the data that you provided:')
        print(cell_phone_3)
    elif my_dice.get_number() == 4:
        print('Here is the data that you provided:')
        print(cell_phone_4)
    elif my_dice.get_number() == 5:
        print('Here is the data that you provided:')
        print(cell_phone_5)
    elif my_dice.get_number() == 6:
        print('Here is the data that you provided:')
        print(cell_phone_6)

    
main()
