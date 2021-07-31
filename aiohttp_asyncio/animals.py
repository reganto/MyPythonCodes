import aiohttp
import asyncio

BASE_URL = "http://127.0.0.1:5000/animals"


async def speak(animal, session):
    async with session.get(f"{BASE_URL}/{animal}") as response:
        response.raise_for_status()
        sound = await response.text()

    return f"The {animal} says '{sound}'."


async def main():
    animals = ["cow", "pig", "chicken"]
    coroutines = []
    async with aiohttp.ClientSession() as session:
        for animal in animals:
            coro = speak(animal, session)
            coroutines.append(coro)

        responses = await asyncio.gather(*coroutines)
    for line in responses:
        print(line)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

