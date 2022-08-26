import sys
import time


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


def snake_speed(text: str, slow_time: float):
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(slow_time)


def snake_field():

    length = 30
    width = 10

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
    print()


snake_field()
snake_speed(f"{MyColors.red + '*'} \n", 1)
