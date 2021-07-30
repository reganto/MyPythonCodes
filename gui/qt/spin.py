import sys
import time
from itertools import cycle


def spin():
    write, flush = sys.stdout.write, sys.stdout.flush

    for char in cycle("|/-\\"):
        write(char)
        flush()
        time.sleep(0.1)
        # \x08 is bachspace
        write("\x08" * len(char))

spin()

