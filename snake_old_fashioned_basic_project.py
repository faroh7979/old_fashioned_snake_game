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

        width = 8
        length = 20

        dimension_list.append(width)
        dimension_list.append(length)

    elif input_size == 'l':

        width = 20
        length = 50

        dimension_list.append(width)
        dimension_list.append(length)

    else:
        width = 12
        length = 30

        dimension_list.append(width)
        dimension_list.append(length)

    return dimension_list


def snake_movement(dimension_list: list):

    width = dimension_list[0]
    length = dimension_list[1]
    total_dimension = length * width
    snake_head_position = total_dimension // 2 - 5
    snake_body_position = []
    snake_body_position_iterable = list(map(str, snake_body_position))
    apple_position_list = []

    for available_apple_positions in range(1, total_dimension + 1):
        if str(available_apple_positions) in snake_body_position_iterable \
                or str(available_apple_positions) in snake_body_position_iterable:
            continue
        apple_position_list.append(available_apple_positions)
    apple_position = random.choice(apple_position_list)

    for quadrant in range(1, total_dimension + 1):

        if quadrant == snake_head_position:
            print(f"{MyColors.sky_blue + '@'}", end='')

        elif quadrant in snake_body_position:
            print(f"{MyColors.sky_blue + '*'}", end='')

        elif quadrant == apple_position:
            print(f"{MyColors.sky_blue + '!'}", end='')

        elif quadrant % length == 1:
            print(f"{MyColors.sky_blue + '|'}", end='')

        elif quadrant % length == 0:
            print(f"{MyColors.sky_blue + '|'}")

        elif 1 < quadrant < length:
            print(f"{MyColors.sky_blue + '‾'}", end='')

        elif 151 < quadrant < total_dimension:
            print(f"{MyColors.sky_blue + '‾'}", end='')

        else:
            print(' ', end='')


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