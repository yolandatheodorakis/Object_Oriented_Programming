import pygame as pg

# Colours
black = pg.Color(0, 0, 0)

# Variables for the game display
screen_width = 500
screen_height = 500

# Initialize pygame
pg.init()

# The screen
window = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('A game of Snake')

# The main loop
run = True
while run:
    # Catches all the events that have happened since the game started
    for event in pg.event.get():
        # When you press the 'close window' button
        if event.type == pg.QUIT:
            run = False
    # Fills the screen with black
    window.fill(black)

# Exits pygame
pg.quit()
