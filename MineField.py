import pygame
import random
import consts
# import Screen

matrix = []

def initialize_matrix():
    for r in range(consts.ROWS):
        row_to_add = []
        for c in range(consts.COLS):
            row_to_add.append(consts.EMPTY)
        matrix.append(row_to_add)

    place_flag()
    place_soldier()
    place_bombs()

    return matrix


def random_index():
    random_row = random.randint(0, consts.ROWS-1)
    random_col = random.randint(0, consts.COLS - consts.BOMB_WIDTH)
    return (random_row, random_col)


def place_flag():
    r_start, c_start = consts.FLAG_START_PLACE
    for r in range(consts.ROWS-2, consts.ROWS - consts.FLAG_WIDTH - 2, -1):
        for c in range(consts.COLS -1, consts.COLS - consts.FLAG_HEIGHT - 2, -1):
            matrix[r][c] == consts.FLAG

def place_soldier():
    r_start, c_start = consts.SOLDIER_START_PLACE
    for r in range(consts.SOLDIER_HEIGHT):
        for c in range(consts.SOLDIER_WIDTH):
            matrix[r][c] = consts.SOLDIER

def place_bombs():
    for i in range(consts.BOMB_COUNT):
        row, col = random_index()
        if is_empty(row, col, consts.BOMB_WIDTH):
            for j in range(consts.BOMB_WIDTH):
                matrix[row][col+j] = consts.BOMB
                

def is_empty(r, c, length):
    for i in range(length):
        if matrix[r][c+i] != consts.EMPTY:
            return False
    
    return True


def update_matrix():
    pass


def is_touching_bomb():
    pass

def is_touching_flag():
    pass

def locate_object(obj):
    pass
