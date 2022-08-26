import sys
import time


def snake_speed(text: str, slow_time: float):
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(slow_time)


snake_speed(f"* \n", 1)
