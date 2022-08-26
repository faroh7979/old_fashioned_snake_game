import sys
import time


def snake_speed(text: str, slow_time: float):
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(slow_time)


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


snake_speed(f"{MyColors.red + '*'} \n", 1)
