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
                Soldier.update_soldier_location(consts.UP, matrix)
                print_matrix(matrix)

            if event.key == pygame.K_DOWN:
                Soldier.update_soldier_location(consts.DOWN, matrix)
                print_matrix(matrix)

            
            if event.key == pygame.K_LEFT:
                Soldier.update_soldier_location(consts.DOWN, matrix)
            
            if event.key == pygame.K_RIGHT:
                Soldier.update_soldier_location(consts.DOWN, matrix)

            if event.key == pygame.K_ENTER:
                print()
                # call to show mine screen

        if event.type == pygame.QUIT:
            pygame.quit()
            game_running = False
        


