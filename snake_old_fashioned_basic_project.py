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

        width = 9
        length = 21

        dimension_list.append(width)
        dimension_list.append(length)

    elif input_size == 'l':

        width = 21
        length = 51

        dimension_list.append(width)
        dimension_list.append(length)

    else:
        width = 13
        length = 31

        dimension_list.append(width)
        dimension_list.append(length)

    return dimension_list


def snake_death_zone(dimension_list: list, death_zone_list: list):

    width = dimension_list[0]
    length = dimension_list[1]
    total_dimension = width * length

    for current_quadrant in range(1, total_dimension + 1):

        if current_quadrant % length == 1 or current_quadrant % length == 0 or \
                1 < current_quadrant < length or total_dimension - length < current_quadrant < total_dimension:
            death_zone_list.append(current_quadrant)

    return death_zone_list


def snake_frame(dimension_list: list, death_zone_list: list):

    width = dimension_list[0]
    length = dimension_list[1]
    total_dimension = length * width

    snake_head_position = (width // 2) * length + length // 2 + 1
    snake_body_position = []
    snake_body_position_iterable = list(map(str, snake_body_position))
    death_zone_list_iterable = list(map(str, death_zone_list))
    apple_position_list = []

    for available_apple_positions in range(1, total_dimension + 1):
        if str(available_apple_positions) in snake_body_position_iterable \
                or str(available_apple_positions) in death_zone_list_iterable \
                or str(available_apple_positions) == str(snake_head_position):
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

        elif quadrant == total_dimension or quadrant == total_dimension - length + 1:
            print(' ', end='')

        elif quadrant % length == 1:
            print(f"{MyColors.sky_blue + '|'}", end='')

        elif quadrant % length == 0:
            print(f"{MyColors.sky_blue + '|'}")

        elif 1 < quadrant < length:
            print(f"{MyColors.sky_blue + '‾'}", end='')

        elif total_dimension - length < quadrant < total_dimension:
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
    death_zone_list = []

    snake_field(dimension_list)
    snake_death_zone(dimension_list, death_zone_list)
    snake_frame(dimension_list, death_zone_list)
    snake_speed(f"{MyColors.red + '*'} \n", 1)
    print(death_zone_list)


game_process()


#for x in range(10):
    #sys.stdout.write(str(x))
    #sys.stdout.flush()
    #time.sleep(5)
    #print(end='\r')