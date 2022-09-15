import pygame
import consts
import random

screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def draw_game():
    screen.fill(consts.BACKGROUND_COLOR)
    draw_grass()
    pygame.display.flip()



def draw_grass():
    print(random_index())

def random_index():
    random_x = random.randint(0, consts.WINDOW_WIDTH)
    random_y = random.randint(0, consts.WINDOW_HEIGHT)
    return tuple((random_x, random_y))


