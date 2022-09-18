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
for r in range(len(matrix)):
    print(matrix[r])
while game_running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('UP')
                # Soldier.update_soldier_location(consts.UP)
            
            if event.key == pygame.K_DOWN:
                print('DOWN')
                # Soldier.update_soldier_location(consts.DOWN)
            
            if event.key == pygame.K_LEFT:
                print('LEFT')
                # Soldier.update_soldier_location(consts.LEFT)
            
            if event.key == pygame.K_RIGHT:
                print('RIGHT')
                # Soldier.update_soldier_location(consts.RIGHT)
        if event.type == pygame.QUIT:
            pygame.quit()
            break


