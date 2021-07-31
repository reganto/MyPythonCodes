#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading
import time
import sys
import itertools


class Signal:
    go = True


def spin(msg: str, signal: Signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('/|-\\'):
        write(char)
        flush()
        write('\x08' * len(char))
        time.sleep(.1)
        if not signal.go:
            break
    write(' ' * len(char) + '\x08' * len(char))


def slow_function() -> int:
    time.sleep(3)
    return 40


def supervisor() -> int:
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('thinking!', signal))
    spinner.start()
    result = slow_function()
    signal.go = False
    return result


def main():
    print(supervisor())


if __name__ == "__main__":
    main()
