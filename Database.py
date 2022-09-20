import pandas as pd
import consts
import os
import ast

file_name = 'game_states.csv'


def initialize_file():
    if os.stat(file_name).st_size == 0:
        game_states = {
            consts.COL_NUMBER: [],
            consts.COL_BOMBS: [],
            consts.COL_SOLDIER: [],
            consts.COL_GRASS: []
        }

        df = pd.DataFrame(game_states)
        df = df.set_index(consts.COL_NUMBER)
        df.to_csv(file_name, mode='a', header=True)


def add_state(num, bomb_indexes, soldier_index, grass_coordinates):
    df = pd.read_csv(file_name)
    # gets the row for the specific num
    data = df.loc[df[consts.COL_NUMBER] == num]
    if not data.empty:
        # overwrite the row with the new values
        df.loc[df[consts.COL_NUMBER] == num] = [num, str(bomb_indexes),
                                                str(soldier_index),
                                                str(grass_coordinates)]
        df.to_csv(file_name, mode='w', index=False)
    else:
        data_to_append = {
            consts.COL_NUMBER: [num],
            consts.COL_BOMBS: [bomb_indexes],
            consts.COL_SOLDIER: [soldier_index],
            consts.COL_GRASS: [grass_coordinates]
        }

        df = pd.DataFrame(data_to_append)
        # a -> append instead of overwrite
        df.to_csv(file_name, mode='a', index=False, header=False)


def read_state(number):
    data = pd.read_csv(file_name)
    wanted_rec = get_record(data, number)
    bombs_list = convert_to_list(wanted_rec[consts.COL_BOMBS])
    grass_list = convert_to_list(wanted_rec[consts.COL_GRASS])
    soldier = convert_to_list(wanted_rec[consts.COL_SOLDIER])
    return [soldier, bombs_list, grass_list]


def get_record(data, number):
    dicts = data.to_dict('records')
    for item in dicts:
        if item[consts.COL_NUMBER] == number:
            return item


def convert_to_list(locations_str):
    return ast.literal_eval(locations_str)
