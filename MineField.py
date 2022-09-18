import pygame
import random
import Screen

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
    random_col = random.randint(0, consts.COLS-1)
    return (random_col, random_row)


def place_flag():
    pass

def place_soldier():
    pass

def place_bombs():
    for i in range(consts.BOMB_COUNT):
        row, col = random_index()
        if is_empty(matrix, row, col, consts.BOMB_WIDTH):
            for j in range(consts.BOMB_WIDTH):
                matrix[row][col+j] = consts.BOMB
                

def is_empty(r, c, length):
    for i in range(length):
        if matrix[r][c+i] != consts.EMPTY:
            return False
    
    return True


def update_matrix(Screen.screen):
    pass


def is_touching_bomb():
    pass

def locate_object(obj):
    pass
