import pygame
import consts
import MineField

def update_soldier_location(movement, matrix):
    matrix = MineField.matrix
    # location_top_left = get_location_body()[0]  # first index of soldier
    locations = [(0,0), (0,1), (1,0), (1,1), (2,0), (2,1), (3,0), (3,1)]
    location_top_left = locations[0]

    if movement == consts.UP:
        new_top_left = (location_top_left[0]-1, location_top_left[1])
            
    if movement == consts.DOWN:
        new_top_left = (location_top_left[0]+1, location_top_left[1])
        
    if movement == consts.LEFT:
        new_top_left = (location_top_left[0], location_top_left[1]-1)
    
    if movement == consts.RIGHT:
        new_top_left = (location_top_left[0], location_top_left[1]+1)
    
    if is_not_out_of_range(new_top_left):
        print(matrix)
        MineField.place_soldier(new_top_left, matrix)



# checks that the soldier is not out of game's bounds
def is_not_out_of_range(new_location):
    new_r, new_c = new_location
    for r in range(consts.SOLDIER_HEIGHT):
        for c in range(consts.SOLDIER_WIDTH):
            if new_r + r < 0 or new_r + r >= consts.ROWS or\
                new_c + c < 0 or new_c >= consts.COLS:
                return False

    return True
    


def is_touching_bomb():
    pass

def is_touching_flag():
    pass


# returns a tuple (row, col)
def get_location_legs():
    pass

# returns a tuple (row, col)
def get_location_body():
    pass


