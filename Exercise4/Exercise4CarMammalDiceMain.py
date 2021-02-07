# File name: Exercise4CarMammalDiceMain.py
# Author: Yolanda Theodorakis
# Description: Create a mammal object. It has the following data attributes: 
#              ID, species, name, size, weight and dimensions (height etc.). 
#              Roll the dice, based on the result check if the correct mammal 
#              (based on ID) fits into your car’s trunk (that you created in 
#              previous task). Also check that your mammal does not exceed the 
#              car’s load limit.

import random

import Exercise4DiceClass as dice
import Exercise4CarClass as car

def main ():

    makes = ['Audi', 'BMW', 'Mercedes-Benz', 'Opel', 'Volkswagen', 'Volvo']
    models = ['A6', 100, 1600, 'V40', 'GT', 'M2']
    mileages = [70000, 500, 230000, 487000, 174000, 300000]
    prices = [34000, 800, 6900, 22000, 13800, 58000]
    colors = ['black', 'white', 'grey', 'beige', 'red', 'blue']
    max_loads = [200, 300, 400, 500, 600, 700]
    trunk_sizes = [1, 2, 3, 4, 5, 6]

    my_car = car.Car(random.choice(makes), random.choice(models), 
                     random.choice(mileages), random.choice(prices), 
                     random.choice(colors), random.choice(max_loads),
                     random.choice(trunk_sizes))

    print(my_car)


main()