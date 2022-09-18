import pygame
import Screen
import Soldier
import MineField
import consts

# TODO: draw element to the screen

# initialize matrix:


game_running = True
while running:
    events = pygame.event
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.KEY_UP:
                Soldier.update_soldier_location(consts.UP)
            
            if event.key == pygame.KEY_DOWN:
                Soldier.update_soldier_location(consts.DOWN)
            
            if event.key == pygame.KEY_LEFT:
                Soldier.update_soldier_location(consts.LEFT)
            
            if event.key == pygame.KEY_RIGHT:
                Soldier.update_soldier_location(consts.RIGHT)


