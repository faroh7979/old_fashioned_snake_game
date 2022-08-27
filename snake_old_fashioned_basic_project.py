import sys
import time
import random


class MyColors:

    pink = '\033[95m'
    blue = '\033[94m'
    sky_blue = '\033[96m'
    ocean_green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    white = '\033[0m'
    bold_white = '\033[1m'
    underline = '\033[4m'


def snake_field(dimension_list: list):

    input_size = input('Please choose your preferred size!')

    if input_size == 's':

        width = 20
        length = 8

        dimension_list.append(width)
        dimension_list.append(length)

    elif input_size == 'l':

        width = 50
        length = 20

        dimension_list.append(width)
        dimension_list.append(length)

    else:
        width = 30
        length = 12

        dimension_list.append(width)
        dimension_list.append(length)

    return dimension_list


def snake_movement(dimension_list: list):

    length = dimension_list[0]
    width = dimension_list[1]
    total_dimension = length * width
    snake_head_position = total_dimension // 2
    snake_body_position = []

    for snake_seal in range(length):

        if snake_seal == 0:
            print(f"{MyColors.sky_blue + '|'}", end='')

        elif snake_seal == length - 1:
            print(f"{MyColors.sky_blue + '‾'}" f"{MyColors.sky_blue + '|'}")

        else:
            print(f"{MyColors.sky_blue + '‾'}", end='')

    for columns in range(width):
        print('|', ' ' * (length - 3), '|')

    for snake_floor in range(length):

        if snake_floor == 0:
            print(f"{MyColors.sky_blue + ' '}", end='')

        elif snake_floor == length - 1:
            print(f"{MyColors.sky_blue + '‾'}", end='')

        else:
            print(f"{MyColors.sky_blue + '‾'}", end='')


def snake_speed(text: str, slow_time: float):

    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(slow_time)


#def snake_position(coordinated_nums: list):


def game_process():
    dimension_list = []

    snake_field(dimension_list)
    snake_movement(dimension_list)
    snake_speed(f"{MyColors.red + '*'} \n", 1)


game_process()


#for x in range(10):
    #sys.stdout.write(str(x))
    #sys.stdout.flush()
    #time.sleep(5)
    #print(end='\r')