from asyncio import sleep
from aiohttp import web

FARM = {
    "cow": "Moo!",
    "pig": "Oink!",
    "chicken": "Cluck!",
}


async def hello(request):
    msg = "Hello, World!"
    return web.Response(text=msg)

async def speak(request):
    animal = request.match_info["name"]
    if animal not in FARM:
        return web.Response(
            text=f"The animal {animal} was not found",
            status=404
        )
    await sleep(4)
    return web.Response(text=FARM[animal])


app = web.Application()
app.router.add_get("/hello/", hello)
resource = app.router.add_resource("/animals/{name}")
resource.add_route("GET", speak)
web.run_app(app)

