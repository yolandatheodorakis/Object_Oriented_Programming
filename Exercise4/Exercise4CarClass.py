# File name: Exercise4CarClass.py
# Author: Yolanda Theodorakis
# Description: Create a car object. It has the following data attributes: make, 
#              model, mileage, price, color, maximum load limit, size of trunk. 
#              Make them private. Write accessor and mutator methods to change 
#              them. Add __str__method to print the state of the car.

class Car:
    # Initialize the states
    def __init__ (self, make, model, mileage, price, color, max_load, trunk_size):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
        self.__color = color
        self.__max_load = max_load
        self.__trunk_size = trunk_size

    # Mutator methods
    def set_make (self, random_make):
        self.__make = random_make

    def set_model (self, random_model):
        self.__model = random_model

    def set_mileage (self, random_mileage):
        self.__mileage = random_mileage

    def set_price (self, random_price):
        self.__price = random_price

    def set_color (self, random_color):
        self.__color = random_color

    def set_max_load (self, random_max_load):
        self.__max_load = random_max_load

    def set_trunk_size (self, random_trunk_size):
        self.__trunk_size = random_trunk_size

    # Accessor methods
    def get_make (self):
        return self.__make

    def get_model (self):
        return self.__model

    def get_mileage (self):
        return self.__mileage

    def get_price (self):
        return self.__price

    def get_color (self):
        return self.__color

    def get_max_load (self):
        return self.__max_load

    def get_trunk_size (self):
        return self.__trunk_size

    # Return the state
    def __str__ (self):
        return ('Make: ' + format(self.__make) + 
                '\nModel: ' + format(self.__model) + 
                '\nMileage: ' + format(self.__mileage) + 
                '\nPrice: ' + format(self.__price) + 
                '\nColor: ' + format(self.__color) + 
                '\nMaximum load limit: ' + format(self.__max_load) + 
                '\nSize of trunk: ' + format(self.__trunk_size))
