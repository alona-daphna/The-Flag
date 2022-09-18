import pygame
import consts
import random
import MineField

screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def draw_game():
    screen.fill(consts.BACKGROUND_COLOR)
    grass_index = draw_grass(random_index())
    pygame.display.flip()


def draw_grass(indexes):
    myimage = pygame.image.load("grass.png")
    myimage = pygame.transform.scale(myimage, (consts.GRASS_WIDTH, consts.GRASS_HEIGHT))
    for item in indexes:
        screen.blit(myimage, item)

def random_index():
    index_list = []
    while len(index_list) != consts.NUM_OF_OBJECTS:
        random_x = random.randint(0, consts.WINDOW_WIDTH - consts.GRASS_WIDTH)
        random_y = random.randint(0, consts.WINDOW_HEIGHT - consts.GRASS_HEIGHT)
        index_tuple = tuple((random_x, random_y))
        if index_tuple not in index_list:
            index_list.append(index_tuple)
    return index_list
