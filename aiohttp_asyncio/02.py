#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio


@asyncio.coroutine
def slow_function():
    yield from asyncio.sleep(10)
    return 40


@asyncio.coroutine
def supervisor():
    a = asyncio.async(slow_function())
    result = yield from slow_function()
    a.cancel()
    return result


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close()
    print(result)


if __name__ == "__main__":
    main()
