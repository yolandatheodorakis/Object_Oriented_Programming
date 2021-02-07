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
import Exercise4MammalClass as mammal

def main ():
    # Random properties for car
    makes = ['Audi', 'BMW', 'Mercedes-Benz', 'Opel', 'Volkswagen', 'Volvo']
    models = ['A6', 100, 1600, 'V40', 'GT', 'M2']
    mileage = random.randint(100, 500000)
    price = random.randint(500, 60000)
    colors = ['black', 'white', 'grey', 'beige', 'red', 'blue']
    max_load = random.randint(200, 1000)
    trunk_size = random.randint(50, 500)

    # Create a car object
    my_car = car.Car(random.choice(makes), random.choice(models), mileage, 
                     price, random.choice(colors), max_load, trunk_size)

    # Random properties for mammal
    species = ['camel', 'dog', 'crow', 'buffalo', 'zebra', 'hippo']
    names = ['Marin', 'Adam', 'Dorothy', 'Lewis', 'Duncan', 'Martha']
    sizes = ['small', 'average', 'big']
    weight = random.randint(10, 1000)
    dimensions = random.randint(50, 500)
    
    # Create mammal objects
    mammal_1 = mammal.Mammal(1, random.choice(species), random.choice(names),
                              random.choice(sizes), weight, dimensions)
    mammal_2 = mammal.Mammal(2, random.choice(species), random.choice(names),
                              random.choice(sizes), weight, dimensions)
    mammal_3 = mammal.Mammal(3, random.choice(species), random.choice(names),
                              random.choice(sizes), weight, dimensions)
    mammal_4 = mammal.Mammal(4, random.choice(species), random.choice(names),
                              random.choice(sizes), weight, dimensions)
    mammal_5 = mammal.Mammal(5, random.choice(species), random.choice(names),
                              random.choice(sizes), weight, dimensions)
    mammal_6 = mammal.Mammal(6, random.choice(species), random.choice(names),
                              random.choice(sizes), weight, dimensions)

    # Create a dice object and roll it
    my_dice = dice.Dice()
    my_dice.roll()

    # Check if the mammal fits in the car
    if my_dice.get_number() == 1:
        if (mammal_1.get_dimensions() <= my_car.get_trunk_size() and 
            mammal_1.get_weight() <= my_car.get_max_load()):
            print(mammal_1.get_name(), 'the', mammal_1.get_species(), 
                  'fits perfectly!')
        elif (mammal_1.get_dimensions() > my_car.get_trunk_size() or 
              mammal_1.get_weight() > my_car.get_max_load()):
              print(mammal_1.get_name(), 'the', mammal_1.get_species(), 
                  'does not fit in the car!')
    elif my_dice.get_number() == 2:
        if (mammal_2.get_dimensions() <= my_car.get_trunk_size() and 
            mammal_2.get_weight() <= my_car.get_max_load()):
            print(mammal_2.get_name(), 'the', mammal_2.get_species(), 
                  'fits perfectly!')
        elif (mammal_2.get_dimensions() > my_car.get_trunk_size() or 
              mammal_2.get_weight() > my_car.get_max_load()):
              print(mammal_2.get_name(), 'the', mammal_2.get_species(), 
                  'does not fit in the car!')
    elif my_dice.get_number() == 3:
        if (mammal_3.get_dimensions() <= my_car.get_trunk_size() and 
            mammal_3.get_weight() <= my_car.get_max_load()):
            print(mammal_3.get_name(), 'the', mammal_3.get_species(), 
                  'fits perfectly!')
        elif (mammal_3.get_dimensions() > my_car.get_trunk_size() or 
              mammal_3.get_weight() > my_car.get_max_load()):
              print(mammal_3.get_name(), 'the', mammal_3.get_species(), 
                  'does not fit in the car!')
    elif my_dice.get_number() == 4:
        if (mammal_4.get_dimensions() <= my_car.get_trunk_size() and 
            mammal_4.get_weight() <= my_car.get_max_load()):
            print(mammal_4.get_name(), 'the', mammal_4.get_species(), 
                  'fits perfectly!')
        elif (mammal_4.get_dimensions() > my_car.get_trunk_size() or 
              mammal_4.get_weight() > my_car.get_max_load()):
              print(mammal_4.get_name(), 'the', mammal_4.get_species(), 
                  'does not fit in the car!')
    elif my_dice.get_number() == 5:
        if (mammal_5.get_dimensions() <= my_car.get_trunk_size() and 
            mammal_5.get_weight() <= my_car.get_max_load()):
            print(mammal_5.get_name(), 'the', mammal_5.get_species(), 
                  'fits perfectly!')
        elif (mammal_5.get_dimensions() > my_car.get_trunk_size() or 
              mammal_5.get_weight() > my_car.get_max_load()):
              print(mammal_5.get_name(), 'the', mammal_5.get_species(), 
                  'does not fit in the car!')
    elif my_dice.get_number() == 6:
        if (mammal_6.get_dimensions() <= my_car.get_trunk_size() and 
            mammal_6.get_weight() <= my_car.get_max_load()):
            print(mammal_6.get_name(), 'the', mammal_6.get_species(), 
                  'fits perfectly!')
        elif (mammal_6.get_dimensions() > my_car.get_trunk_size() or 
              mammal_6.get_weight() > my_car.get_max_load()):
              print(mammal_6.get_name(), 'the', mammal_6.get_species(), 
                  'does not fit in the car!')

main()
