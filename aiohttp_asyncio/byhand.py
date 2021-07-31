import asyncio


async def square(x):
    print(f"Starting square for {x}")
    if x == 7:
        raise ValueError("wtf 7!!!")
    await asyncio.sleep(3)
    print(f"Finishing square for {x}.")
    return x * x


async def cube(x):
    print(f"Starting cube for {x}")
    await asyncio.sleep(3)
    y = await square(x)
    print(f"Finishing cube for {x}")
    return y * x

