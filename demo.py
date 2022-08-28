import sys
import time
for x in range(10):
    sys.stdout.write(f"{'*' * 1000} \n )")
    sys.stdout.flush()
    time.sleep(2)
    print(end='\r')
    x = input()