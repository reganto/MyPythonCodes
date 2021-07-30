import asyncio
import time


async def func1():
    print('Start func1')
    print('wait in func1')
    await asyncio.sleep(5)
    print('func1 finish') 


async def func2():
    print('Start func2')
    print('yet in func2')
    x = 2 + 3
    # for i in range(100):
    #     x += i
    print('wait in func2')
    await asyncio.sleep(5)
    print('after wait in func2')
    print('func2 finish')


async def main():
    await asyncio.gather(func1(), func2())


if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
