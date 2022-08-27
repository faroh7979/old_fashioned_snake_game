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


def snake_field():
    input_size = input('Please choose your preferred size!')

    if input_size == 's':
        width = 20
        length = 8
    elif input_size == 'l':
        width = 50
        length = 20
    else:
        width = 30
        length = 12

    return width, length


def snake_movement(length: int, width: int):

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
    length = 0
    width = 0

    snake_field()
    snake_speed(f"{MyColors.red + '*'} \n", 1)





#for x in range(10):
    #sys.stdout.write(str(x))
    #sys.stdout.flush()
    #time.sleep(5)
    #print(end='\r')