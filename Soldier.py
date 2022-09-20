import pygame
import Screen
import consts
import MineField


def update_soldier_location(movement, grass, matrix):
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

        if is_touching_bomb(new_top_left):
            hit_object = consts.BOMB

        elif is_touching_flag(matrix, new_top_left):
            hit_object = consts.FLAG

        else:
            MineField.remove_soldier(matrix)
            MineField.place_soldier(matrix, new_top_left)

        Screen.create_player(new_top_left, grass)

    return hit_object


# checks that the soldier is not out of game's bounds
def is_not_out_of_range(new_location):
    new_r, new_c = new_location
    for r in range(consts.SOLDIER_HEIGHT):
        for c in range(consts.SOLDIER_WIDTH):
            if (new_r + r < 0 or new_r + r >= consts.ROWS) or \
                    (new_c + c < 0 or new_c + c >= consts.COLS):
                return False

    return True


def is_touching_bomb(new_location):
    new_r, new_c = new_location
    bomb_locations = MineField.get_object_location(consts.BOMB)
    leg_row = new_r + consts.SOLDIER_HEIGHT - 1
    for col in range(consts.SOLDIER_WIDTH):
        if (leg_row, new_c + col) in bomb_locations:
            return True
    return False


def is_touching_flag(matrix, new_location):
    MineField.place_soldier(matrix, new_location)
    flag_locations = MineField.get_object_location(consts.FLAG)
    if len(flag_locations) <= consts.FLAG_HEIGHT * consts.FLAG_WIDTH - 4:
        return True
    return False