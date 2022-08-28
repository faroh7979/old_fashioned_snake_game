import sys
import time
import random
from threading import Timer


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

        width = 4
        length = 10
        snake_head_position = (width // 2) * length + length // 2 + 1

        dimension_list.append(width)
        dimension_list.append(length)
        dimension_list.append(snake_head_position)

        # It is about definition of apple position
        dimension_list.append(False)

        # It is about fictive apple position for first loop
        dimension_list.append(0)

    elif input_size == 'l':

        width = 21
        length = 51
        snake_head_position = (width // 2) * length + length // 2 + 1

        dimension_list.append(width)
        dimension_list.append(length)
        dimension_list.append(snake_head_position)

        # It is about definition of apple position
        dimension_list.append(False)

        # It is about fictive apple position for first loop
        dimension_list.append(0)

    else:
        width = 13
        length = 31
        snake_head_position = (width // 2) * length + length // 2 + 1

        dimension_list.append(width)
        dimension_list.append(length)
        dimension_list.append(snake_head_position)

        # It is about definition of apple position
        dimension_list.append(False)

        # It is about fictive apple position for first loop
        dimension_list.append(0)

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


def snake_frame(snake_head_tracking_record, total_body_pieces, snake_body_position: list, direction: str, frame_list: list, dimension_list: list, death_zone_list: list):

    width = dimension_list[0]
    length = dimension_list[1]
    snake_head_position = dimension_list[2]
    apple_position = dimension_list[4]
    total_dimension = length * width

    death_zone_list_iterable = list(map(str, death_zone_list))
    apple_position_list = []

    if not snake_head_tracking_record:
        snake_head_tracking_record.append(snake_head_position)

    if direction == 'w':
        snake_head_position -= length
        snake_head_tracking_record.insert(0, snake_head_position)
        dimension_list.pop(2)
        dimension_list.insert(2, snake_head_position)
        if snake_head_position == apple_position:
            dimension_list.pop(3)
            dimension_list.insert(3, False)
            total_body_pieces[0] += 1
            for current_index in range(0, total_body_pieces[0] + 1):
                snake_body_position.append(snake_head_tracking_record[current_index])

        else:
            for current_index in range(0, total_body_pieces[0] + 1):
                snake_body_position.append(snake_head_tracking_record[current_index])

    elif direction == 's':
        snake_head_position += length
        snake_head_tracking_record.insert(0, snake_head_position)
        dimension_list.pop(2)
        dimension_list.insert(2, snake_head_position)
        if snake_head_position == apple_position:
            dimension_list.pop(3)
            dimension_list.insert(3, False)
            total_body_pieces[0] += 1
            for current_index in range(0, total_body_pieces[0] + 1):
                snake_body_position.append(snake_head_tracking_record[current_index])

        else:
            for current_index in range(0, total_body_pieces[0] + 1):
                snake_body_position.append(snake_head_tracking_record[current_index])

    elif direction == 'd':
        snake_head_position += 1
        snake_head_tracking_record.insert(0, snake_head_position)
        dimension_list.pop(2)
        dimension_list.insert(2, snake_head_position)
        if snake_head_position == apple_position:
            dimension_list.pop(3)
            dimension_list.insert(3, False)
            total_body_pieces[0] += 1
            for current_index in range(0, total_body_pieces[0] + 1):
                snake_body_position.append(snake_head_tracking_record[current_index])

        else:
            for current_index in range(0, total_body_pieces[0] + 1):
                snake_body_position.append(snake_head_tracking_record[current_index])

    elif direction == 'a':
        snake_head_position -= 1
        snake_head_tracking_record.insert(0, snake_head_position)
        dimension_list.pop(2)
        dimension_list.insert(2, snake_head_position)
        if snake_head_position == apple_position:
            dimension_list.pop(3)
            dimension_list.insert(3, False)
            total_body_pieces[0] += 1
            for current_index in range(0, total_body_pieces[0] + 1):
                snake_body_position.append(snake_head_tracking_record[current_index])

        else:
            for current_index in range(0, total_body_pieces[0] + 1):
                snake_body_position.append(snake_head_tracking_record[current_index])

    snake_body_position_iterable = list(map(str, snake_body_position))

    apple_position_found = dimension_list[3]

    if not apple_position_found:

        for available_apple_positions in range(1, total_dimension + 1):
            if str(available_apple_positions) in snake_body_position_iterable \
                    or str(available_apple_positions) in death_zone_list_iterable \
                    or str(available_apple_positions) == str(snake_head_position):
                continue
            apple_position_list.append(available_apple_positions)

        apple_position = random.choice(apple_position_list)
        dimension_list.pop(3)
        dimension_list.insert(3, True)
        dimension_list.pop(4)
        dimension_list.append(apple_position)

    for quadrant in range(1, total_dimension + 1):

        if quadrant == snake_head_position:
            frame_list.append(f"{MyColors.pink + '@'}")

        elif quadrant in snake_body_position:
            frame_list.append(f"{MyColors.sky_blue + '*'}")

        elif quadrant == apple_position:
            frame_list.append(f"{MyColors.red + '!'}")

        elif quadrant == total_dimension or quadrant == total_dimension - length + 1:
            frame_list.append(' ')

        elif quadrant % length == 1:
            frame_list.append(f"{MyColors.sky_blue + '|'}")

        elif quadrant % length == 0:
            frame_list.append(f"{MyColors.sky_blue + '|'} \n")

        elif 1 < quadrant < length:
            frame_list.append(f"{MyColors.sky_blue + '‾'}")

        elif total_dimension - length < quadrant < total_dimension:
            frame_list.append(f"{MyColors.sky_blue + '‾'}")

        else:
            frame_list.append(' ')

    return frame_list, dimension_list, snake_body_position, snake_head_tracking_record, total_body_pieces


def snake_speed(text: str, slow_time: float):

    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(slow_time)
    print(end='\r')


def game_process():
    dimension_list = []
    death_zone_list = []

    snake_head_tracking_record = []
    total_body_pieces = [0]

    direction = ''

    snake_field(dimension_list)
    snake_death_zone(dimension_list, death_zone_list)

    while True:
        frame_list = []
        snake_body_position = []

        snake_frame(snake_head_tracking_record, total_body_pieces, snake_body_position, direction, frame_list, dimension_list, death_zone_list)
        frame_string = ''.join(frame_list)

        print(frame_string)
        print(end='\r' * 1000)

        # timeout = 10
        # t = Timer(timeout, print, [frame_string])
        # t.start()
        # prompt = "You have %d seconds to choose the correct answer...\n" % timeout
        # direction_input = input(prompt)
        direction_input = input()
        if direction_input:
            direction = direction_input
        if direction == 'q':
            break
        # t.cancel()


game_process()
