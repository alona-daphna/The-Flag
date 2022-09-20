import pygame
import consts
import MineField
import time

screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def draw_game(grass):
    draw_grass(grass)
    draw_text()
    draw_flag(consts.FLAG_PATH)
    create_player(MineField.get_object_location(consts.SOLDIER)[0], grass)


def create_player(coordinates, grass, img=consts.SOLDIER_PATH):
    if (img == consts.SOLDIER_PATH):
        draw_grass(grass)
        draw_flag(consts.FLAG_PATH)
        draw_text()
    y, x = coordinates
    x *= consts.WIDTH_MULTIPLIER
    y *= consts.WIDTH_MULTIPLIER
    soldier_img = pygame.image.load(img)
    soldier_img = pygame.transform.scale(soldier_img,
                                         (consts.SOLDIER_WIDTH_PIXEL,
                                          consts.SOLDIER_HEIGHT_PIXEL))
    screen.blit(soldier_img, (x, y))
    pygame.display.flip()


def present_bomb_screen(grass):
    screen.fill(consts.BLACK)
    draw_grid()
    create_player(MineField.get_object_location(consts.SOLDIER)[0], grass,
                  consts.SOLDIER_NIGHT_PATH)
    draw_bombs(MineField.get_bomb_locations())
    time.sleep(1)


def draw_grid():
    for row in range(0, consts.WINDOW_WIDTH, consts.HEIGHT_MULTIPLIER):
        for col in range(0, consts.WINDOW_HEIGHT, consts.WIDTH_MULTIPLIER):
            rect = pygame.Rect(row, col, 20, 20)
            pygame.draw.rect(screen, consts.GREEN, rect, 1)

def draw_bombs(bomb_coordinates):
    myimage = pygame.image.load(consts.BOMB_PATH)
    myimage = pygame.transform.scale(myimage,
                                     (consts.BOMB_WIDTH_PIXEL,
                                      consts.BOMB_HEIGHT_PIXEL))
    draw_objects(bomb_coordinates, myimage)


def draw_grass(grass_coordinates):
    screen.fill(consts.BACKGROUND_COLOR)
    myimage = pygame.image.load(consts.GRASS_PATH)
    myimage = pygame.transform.scale(myimage,
                                     (consts.GRASS_WIDTH, consts.GRASS_HEIGHT))
    draw_objects(grass_coordinates, myimage)


def draw_text():
    pygame.font.init()
    my_font = pygame.font.SysFont(consts.FONT_NAME, 15, bold=True)
    text = my_font.render('Welcome to The Flag game', True,
                          consts.WHITE)
    screen.blit(text, (80, 20))
    text = my_font.render('Have fun!', True, consts.WHITE)
    screen.blit(text, (80, 40))
    pygame.display.flip()


def draw_flag(image_path):
    flag_image = pygame.image.load(image_path)
    flag_image = pygame.transform.scale(flag_image, (consts.FLAG_WIDTH_PIXEL,
                                                     consts.FLAG_HEIGHT_PIXEL))
    x = consts.WINDOW_WIDTH - consts.FLAG_WIDTH_PIXEL
    y = consts.WINDOW_HEIGHT - consts.FLAG_HEIGHT_PIXEL
    screen.blit(flag_image, (x, y))


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


def draw_message(message, font_size, color, location):
    pygame.font.init()
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)
    pygame.display.flip()


def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)
