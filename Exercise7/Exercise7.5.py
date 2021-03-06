# File name: Exercise7.5.py
# Author: Yolanda Theodorakis
# Description: Implement the following UML diagram. Try to figure out the best 
#              way to have animals in appropriate data structure in the 
#              Student class. Think, do you need to have the owner of the pet 
#              information in the Pet class (in order to make the relationship 
#              between Student and Pet). If yes, add that.

class Student:
    def __init__(self, first_name, last_name, student_ID):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_ID = student_ID
        self.__pets = []

        def set_first_name(self, first_name):
            self.__first_name = first_name

        def get_first_name(self):
            return self.__first_name

        def set_last_name(self, last_name):
            self.__last_name = last_name

        def get_last_name(self):
            return self.__last_name

        def set_student_ID(self, student_ID):
            self.__student_ID = student_ID

        def get_student_ID(self):
            return self.__student_ID

        def add_pets(self, species, name):
            self.__pets.append(Pet(species, name))

        def remove_pets(self):
            self.__pets.pop()

        def print_pets(self):
            return self.__pets

        def __str__(self):
            return ('Student named {} {}, {}, has these pets: {}.'
            .format(self.__first_name, self.last_name, self.__student_ID, self.__pets))

class Pet:
    def __init__(self, species, name):
        self.__species = species
        self.__name = name

    def set_species(self, species):
        self.__species = species

    def get_species(self):
        return self.__species

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def __str__(self):
        return 'A/an {} named {}.'.format(self.__species, self.__name)


