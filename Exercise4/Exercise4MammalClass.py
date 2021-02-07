# File name: Exercise4MammalClass.py
# Author: Yolanda Theodorakis
# Description: Create a mammal object. It has the following data attributes: 
#              ID, species, name, size, weight and dimensions (height etc.). 
#              Roll the dice, based on the result check if the correct mammal 
#              (based on ID) fits into your car’s trunk (that you created in 
#              previous task). Also check that your mammal does not exceed the 
#              car’s load limit.

class Mammal:
    # Initialize the states
    def __init__ (self, ID, species, name, size, weight, dimensions):
        self.__id = ID
        self.__species = species
        self.__name = name
        self.__size = size
        self.__weight = weight
        self.__dimensions = dimensions

    # Mutator methods
    def set_id (self, random_ID):
        self.__id = random_ID

    def set_species (self, random_species):
        self.__species = random_species

    def set_name (self, random_name):
        self.__name = random_name

    def set_size (self, random_size):
        self.__size = random_size

    def set_weight (self, random_weight):
        self.__weight = random_weight

    def set_dimensions (self, random_dimensions):
        self.__dimensions = random_dimensions

    # Accessor methods
    def get_id (self):
        return self.__id

    def get_species (self):
        return self.__species

    def get_name (self):
        return self.__name

    def get_size (self):
        return self.__size

    def get_weight (self):
        return self.__weight

    def get_dimensions (self):
        return self.__dimensions
