#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
import itertools
import sys


@asyncio.coroutine
def spin1(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    write(' ' * len(status) + '\x08' * len(status))


@asyncio.coroutine
def spin2(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    write(' ' * len(status) + '\x08' * len(status))


@asyncio.coroutine
def slow_function():
    yield from asyncio.sleep(3)
    return 43


@asyncio.coroutine
def simple_function():
    try:
        yield from asyncio.sleep(2)
        print('\nsimple function done\n')
    except asyncio.CancelledError:
        exit(1)


@asyncio.coroutine
def sample_function():
    try:
        yield from asyncio.sleep(1.5)
        print('\nsample function done\n')
    except asyncio.CancelledError:
        exit(1)
        

@asyncio.coroutine
def supervisor():
    task1 = asyncio.Task(spin1('thinking!'))
    task2 = asyncio.Task(simple_function())
    task3 = asyncio.Task(sample_function())
    print('task1 object:', task1)
    print('task2 object:', task2)
    print('task3 object:', task3)
    result = yield from slow_function()
    task1.cancel()
    task2.cancel()
    task3.cancel()
    return result


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close()
    print('Answer:', result)


if __name__ == "__main__":
    main()
