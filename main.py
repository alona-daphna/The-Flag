import Screen
import consts
import pygame
import time
import MineField
import Soldier
import Database


def main():
    pygame.init()
    game_running = True
    matrix = MineField.initialize_matrix(consts.SOLDIER_START_PLACE)
    grass = MineField.get_grass_locations()
    Screen.draw_game(grass)
    hit_object = ''
    Database.initialize_file()
    while game_running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 \
                        or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9:
                    duration = get_time(event)
                    action = get_action_type(duration)
                    if action == consts.SAVE:
                        print("SAVING")
                        Database.add_state(
                                int(chr(event.key)),
                                MineField.get_object_location(consts.BOMB),
                                MineField.get_object_location(consts.SOLDIER)[
                                    0],
                                grass)
                    else:
                        print("LOADING...")
                        game_data = Database.read_state(int(chr(event.key)))

                        soldier = game_data[0]
                        bombs_locations = game_data[1]
                        grass = game_data[2]
                        matrix = MineField.initialize_matrix(soldier, bombs_locations)
                        Screen.draw_game(grass)

                if event.key == pygame.K_UP:
                    hit_object = Soldier.update_soldier_location(consts.UP, grass,
                                                                 matrix)
                if event.key == pygame.K_DOWN:
                    hit_object = Soldier.update_soldier_location(consts.DOWN, grass,
                                                                 matrix)

                if event.key == pygame.K_LEFT:
                    hit_object = Soldier.update_soldier_location(consts.LEFT, grass,
                                                                 matrix)

                if event.key == pygame.K_RIGHT:
                    hit_object = Soldier.update_soldier_location(consts.RIGHT, grass,
                                                                 matrix)

                if event.key == pygame.K_RETURN:
                    Screen.present_bomb_screen(grass)
                    Screen.draw_game(grass)
                    pygame.event.clear(eventtype=pygame.KEYDOWN)

            if event.type == pygame.QUIT:
                pygame.quit()
                game_running = False

            if len(hit_object) > 0:
                if hit_object == consts.BOMB:
                    Screen.draw_lose_message()
                if hit_object == consts.FLAG:
                    Screen.draw_win_message()
                game_running = False
                time.sleep(3)
    pygame.quit()


def get_time(event):
    current_time = time.time()
    is_key_pressed = True
    while is_key_pressed:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYUP:
                up_time = time.time()
                is_key_pressed = False
    return up_time - current_time


def get_action_type(time):
    return consts.LOAD if time > 1 else consts.SAVE


def print_matrix(matrix):
    for r in range(len(matrix)):
        print(matrix[r])


if __name__ == '__main__':
    main()
