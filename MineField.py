import consts
import random

matrix = []


def initialize_matrix():
    for r in range(consts.ROWS):
        row_to_add = []
        for c in range(consts.COLS):
            row_to_add.append(consts.EMPTY)
        matrix.append(row_to_add)

    place_flag()
    place_soldier(matrix)
    place_bombs()

    return matrix


def random_index():
    random_row = random.randint(0, consts.ROWS - 1)
    random_col = random.randint(0, consts.COLS - consts.BOMB_WIDTH)
    return (random_row, random_col)


def place_flag():
    r_start, c_start = consts.FLAG_START_PLACE
    for r in range(consts.ROWS - 2, consts.ROWS - consts.FLAG_WIDTH - 1, -1):
        for c in range(consts.COLS - 1, consts.COLS - consts.FLAG_HEIGHT - 2,
                       -1):
            matrix[r][c] = consts.FLAG


def place_soldier(matrix, location_start=consts.SOLDIER_START_PLACE):
    r_start, c_start = location_start
    for r in range(consts.SOLDIER_HEIGHT):
        for c in range(consts.SOLDIER_WIDTH):
            matrix[r_start+r][c_start+c] = consts.SOLDIER


def place_bombs():
    count = 0
    while count != 20:
        row, col = random_index()
        if is_empty(row, col, consts.BOMB_WIDTH):
            for j in range(consts.BOMB_WIDTH):
                matrix[row][col + j] = consts.BOMB
            count += 1


def is_empty(r, c, length):
    for i in range(length):
        if matrix[r][c + i] != consts.EMPTY:
            return False

    return True

def get_object_location(obj):
    indexes = []
    for r in range(consts.ROWS):
        for c in range(consts.COLS):
            if matrix[r][c] == obj:
                indexes.append((r, c))
    return indexes


def get_player_location():
    for row in range(consts.ROWS):
        for col in range(consts.COLS):
            return ((col, row))


# returns a list of tuples [(row, col)]
def get_bomb_locations():
    indexes = []
    for r in range(consts.ROWS):
        for c in range(consts.COLS):
            if matrix[r][c] == consts.BOMB:
                indexes.append((c * consts.HEIGHT_MULTIPLIER,
                                r * consts.WIDTH_MULTIPLIER))

    locations_by_first_index = []
    for i in range(0, len(indexes), 3):
        locations_by_first_index.append(indexes[i])

    return locations_by_first_index

def get_grass_locations():
    index_list = []
    while len(index_list) != consts.NUM_OF_OBJECTS:
        random_x = random.randint(0, consts.WINDOW_WIDTH - consts.GRASS_WIDTH)
        random_y = random.randint(0,
                                  consts.WINDOW_HEIGHT - consts.GRASS_HEIGHT)
        index_tuple = tuple((random_x, random_y))
        if index_tuple not in index_list:
            index_list.append(index_tuple)
    return index_list

def remove_soldier(matrix):
    for r in range(consts.ROWS):
        for c in range(consts.COLS):
            if matrix[r][c] == consts.SOLDIER:
                matrix[r][c] = consts.EMPTY