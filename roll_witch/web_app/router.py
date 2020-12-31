from aiohttp import web
from . import roller


async def handle(request):
    text = "Hello"
    return web.Response(text=text)


async def start_app():
    app = web.Application()
    app.router.add_get("/", handle)
    app.router.add_post("/", roller.roll)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()
