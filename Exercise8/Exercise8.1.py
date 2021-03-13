# File  name: Exercise8.1.py
# Author: Yolanda Theodorakis
# Description: Cleaning the flat

class Flat:
    # Initialize the states
    def __init__(self):
        self.floors = 'dirty'
        self.windows = 'dirty'
        self.surfaces = 'dirty'
        self.bed = 'unmade'
        self.fridge = 'empty'
        self.toilet_paper = '1 roll'

    def wash_windows(self):
        self.windows = 'clean'

    def get_windows(self):
        return self.windows

    def make_bed(self):
        self.bed = 'made'

    def get_bed(self):
        return self.bed

    def vacuum(self):
        self.floors = 'clean'

    def get_floors(self):
        return self.floors

    def dust(self):
        self.surfaces = 'clean'

    def get_surfaces(self):
        return self.surfaces

    def do_groceries(self):
        self.fridge = 'full'

    def get_fridge(self):
        return self.fridge

    def hoard_toilet_paper(self):
        self.toilet_paper = '100 rolls'

    def get_toilet_paper(self):
        return self.toilet_paper

    def __str__(self):
        return ('The floors are {}, the windows are {}, \
                 \nand the surfaces are {}. The bed is {}. \
                 \nThe fridge is {} and I have {} of toilet paper.'
                .format(self.floors, self.windows, self.surfaces, self.bed, 
                self.fridge, self.toilet_paper))


def main():
    # Create a new object
    my_flat = Flat()

    # Let's see in what state my flat is
    print(my_flat)

    # Wash the windows and make the bed
    print('\nI will clean the windows and make the bed now...')
    my_flat.wash_windows()
    my_flat.make_bed()
    print('The windows are now {} and bed is {}.'
          .format(my_flat.get_windows(), my_flat.get_bed()))

    # Vacuum and dust
    print('\nI will vacuum the floors and dust the surfaces now...')
    my_flat.vacuum()
    my_flat.dust()
    print('The floors are now {} and the surfaces are {}.'
          .format(my_flat.get_floors(), my_flat.get_surfaces()))

    # Do groceries
    print('\nI will do the groceries now...')
    my_flat.do_groceries()
    print('The fridge is {}.'.format(my_flat.get_fridge()))

    # Hoard toilet paper
    print('\nFinally, I will buy some toilet paper...')
    my_flat.hoard_toilet_paper()
    print('I now have {} of toilet paper.\n'.format(my_flat.get_toilet_paper()))

    # Final state
    print(my_flat)


main()
