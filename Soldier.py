import pygame

import Screen
import consts
import MineField


def update_soldier_location(movement, matrix):
    hit_object = ''
    matrix = MineField.matrix
    # location_top_left = get_location_body()[0]  # first index of soldier
    locations = MineField.get_object_location(consts.SOLDIER)
    location_top_left = locations[0]

    if movement == consts.UP:
        new_top_left = (location_top_left[0] - 1, location_top_left[1])

    if movement == consts.DOWN:
        new_top_left = (location_top_left[0] + 1, location_top_left[1])

    if movement == consts.LEFT:
        new_top_left = (location_top_left[0], location_top_left[1] - 1)

    if movement == consts.RIGHT:
        new_top_left = (location_top_left[0], location_top_left[1] + 1)

    if is_not_out_of_range(new_top_left):
        MineField.remove_soldier(matrix)

        if is_touching_bomb(new_top_left):
            hit_object = consts.BOMB
        if is_touching_flag():
            hit_object = consts.FLAG
        MineField.place_soldier(matrix, new_top_left)
        Screen.create_player(new_top_left)
    return hit_object

# checks that the soldier is not out of game's bounds
def is_not_out_of_range(new_location):
    new_r, new_c = new_location
    for r in range(consts.SOLDIER_HEIGHT):
        for c in range(consts.SOLDIER_WIDTH):
            if new_r + r < 0 or new_r + r >= consts.ROWS or \
                    new_c + c < 0 or new_c >= consts.COLS:
                return False

    return True


def is_touching_bomb(new_location):
    new_r, new_c = new_location
    locations = MineField.get_object_location(consts.BOMB)
    matrix = MineField.matrix
    leg_row = new_r+consts.SOLDIER_HEIGHT-1
    for col in range(consts.SOLDIER_WIDTH):
        if matrix[new_r][new_c+col] == consts.BOMB:
            return True
    return False


def is_touching_flag():
    count = 0
    flag_locations = MineField.get_object_location(consts.FLAG)
    player_locations = MineField.get_object_location(consts.SOLDIER)
    if len(player_locations) > 0:
        if player_locations[0] in flag_locations and player_locations[1] in flag_locations:
            return True
        for item in player_locations:
            if item in flag_locations:
                count += 1
        if count >= 4:
            return True
    return False


# returns a tuple (row, col)
def get_location_legs():
    pass
