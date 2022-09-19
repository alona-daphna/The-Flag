import pygame
import consts
import random
import MineField
import time

screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def draw_game():
    coordinates = random_coordinates()
    draw_grass(coordinates)
    create_player(MineField.get_player_location())


def create_player(coordinates, img = "imgs/soldier.png"):
    y, x = coordinates
    x *= consts.WIDTH_MULTIPLIER
    y *= consts.WIDTH_MULTIPLIER
    soldier_img = pygame.image.load(img)
    soldier_img = pygame.transform.scale(soldier_img, (consts.SOLDIER_WIDTH_PIXEL,
                                           consts.SOLDIER_HEIGHT_PIXEL))
    screen.blit(soldier_img, (x,y))
    pygame.display.flip()


def present_bomb_screen():
    screen.fill(consts.BLACK)
    draw_grid()
    create_player(MineField.get_player_location(), "imgs/soldier_night.png")
    draw_bombs(MineField.get_bomb_locations())
    time.sleep(1)


def draw_grid():
    for row in range(0, consts.WINDOW_WIDTH, consts.HEIGHT_MULTIPLIER):
        for col in range(0, consts.WINDOW_HEIGHT, consts.WIDTH_MULTIPLIER):
            rect = pygame.Rect(row, col, 20, 20)
            pygame.draw.rect(screen, consts.GREEN, rect, 1)


def draw_bombs(bomb_coordinates):
    myimage = pygame.image.load("imgs/bomb.png")
    myimage = pygame.transform.scale(myimage,
                                     (consts.BOMB_WIDTH_PIXEL,
                                      consts.BOMB_HEIGHT_PIXEL))
    draw_objects(bomb_coordinates, myimage)


def draw_grass(grass_coordinates):
    screen.fill(consts.BACKGROUND_COLOR)
    myimage = pygame.image.load("imgs/grass.png")
    myimage = pygame.transform.scale(myimage,
                                     (consts.GRASS_WIDTH, consts.GRASS_HEIGHT))
    draw_objects(grass_coordinates, myimage)

def draw_objects(coordinates, image):
    for coordinate in coordinates:
        screen.blit(image, coordinate)
    pygame.display.flip()


def get_coordinates_bomb(matrix):
    coordinates = []
    for row in range(consts.ROWS):
        for col in range(consts.COLS):
            if matrix[row][col] == consts.BOMB:
                coordinates.append((row, col))
    return coordinates


def random_coordinates():
    index_list = []
    while len(index_list) != consts.NUM_OF_OBJECTS:
        random_x = random.randint(0, consts.WINDOW_WIDTH - consts.GRASS_WIDTH)
        random_y = random.randint(0,
                                  consts.WINDOW_HEIGHT - consts.GRASS_HEIGHT)
        index_tuple = tuple((random_x, random_y))
        if index_tuple not in index_list:
            index_list.append(index_tuple)
    return index_list
