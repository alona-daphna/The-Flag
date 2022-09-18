import Screen
import consts
import pygame
import time
import MineField
import Soldier

def main():
    pygame.init()
    game_running = True
    matrix = MineField.initialize_matrix()
    Screen.draw_game()
    hit_object = ''
    while game_running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("before")
                    hit_object = Soldier.update_soldier_location(consts.UP,
                                                                 matrix)
                    print("after")
                if event.key == pygame.K_DOWN:
                    hit_object = Soldier.update_soldier_location(consts.DOWN,
                                                                 matrix)

                if event.key == pygame.K_LEFT:
                    hit_object = Soldier.update_soldier_location(consts.LEFT,
                                                                 matrix)

                if event.key == pygame.K_RIGHT:
                    hit_object = Soldier.update_soldier_location(consts.RIGHT,
                                                                 matrix)

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

def print_matrix(matrix):
    for r in range(len(matrix)):
        print(matrix[r])

if __name__ == '__main__':
    main()