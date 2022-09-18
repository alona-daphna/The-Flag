import pygame
import Screen
import Soldier
import MineField
import consts

# TODO: draw element to the screen

# initialize matrix:

pygame.init()
game_running = True
matrix = MineField.initialize_matrix()
def print_matrix(matrix):
    for r in range(len(matrix)):
        print(matrix[r])
    
while game_running:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                hit_object = Soldier.update_soldier_location(consts.UP, matrix)

            if event.key == pygame.K_DOWN:
                hit_object = Soldier.update_soldier_location(consts.DOWN, matrix)

            
            if event.key == pygame.K_LEFT:
                hit_object = Soldier.update_soldier_location(consts.LEFT, matrix)
            
            if event.key == pygame.K_RIGHT:
                hit_object = Soldier.update_soldier_location(consts.RIGHT, matrix)

            if event.key == pygame.K_RETURN:
                print()
                # call to show mine screen

        if event.type == pygame.QUIT:
            pygame.quit()
            game_running = False

        if len(hit_object) > 0:
            if hit_object == consts.BOMB:
                pass
                # hit bomb
            if hit_object == consts.FLAG:
                pass
                # win
        


