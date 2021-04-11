# File  name: Game.py
# Author: Yolanda Theodorakis
# Description: Snake game

import pygame as pg
import Snake as snake
import Food as food

# Variables for the game display
screen_width = 500
screen_height = 500

# Colors
black = pg.Color(0, 0, 0)
white = pg.Color(255, 255, 255)

# Variables for scrores
score, high_score = (0, 0)

# Draws the score on the screen
def show_score(surface):
    global high_score
    font_name = pg.font.match_font('arial')
    if score > high_score:
        high_score = score
    # Writing the score
    font = pg.font.Font(font_name, 18)
    text_surface = font.render('Score: {} High Score: {}'.format(score, high_score), True, white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (200, 10)
    surface.blit(text_surface, text_rect)

# What to do when the game is over
def game_over():
    global score
    # Write 'game over' to the screen
    game_over_font = pg.font.Font('freesansbold.ttf', 24)
    game_over_surface = game_over_font.render('Game Over', True, white)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (200, 50)
    window.blit(game_over_surface, game_over_rect)
    # Reset score
    score = 0
    pg.display.flip()
    time.sleep(2)
    # Re-initialize game
    run = True
    fd = food.Food()
    s = snake.Snake()
    play_game(fd, s)

# The game
def play_game(food_object, snake_object):
    global score
    run = True
    while run:
        # FPS
        clock = pg.time.Clock()
        clock.tick(30)
        # Catches all the events that have happened since the game started
        for event in pg.event.get():
            # When you press the 'close window' button
            if event.type == pg.QUIT:
                run = False
        # Draw food and snake to the screen and show score
        window.fill(black)
        food_object.draw_food(window)
        snake_object.draw_snake(window)
        show_score(window)
        # User input
        pressed = pg.key.get_pressed()
        if pressed[pg.K_UP]:
            snake_object.change_direction('up')
        if pressed[pg.K_LEFT]:
            snake_object.change_direction('left')
        if pressed[pg.K_DOWN]:
            snake_object.change_direction('down')
        if pressed[pg.K_RIGHT]:
            snake_object.change_direction('right')
        # Move the snake
        snake_object.move()
        # Eat
        if food_object.is_eaten(snake_object.head):
            food_object.new_position()
            snake_object.increase_length()
            score += 10
        # Collision
        if snake_object.is_collision():
            run = False
            game_over()
        pg.display.update()

# Initialize pygame
pg.init()

# The screen
window = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('A game of Snake')
fd = food.Food()
s = snake.Snake()
play_game(fd, s)

# Exits pygame
pg.quit()
