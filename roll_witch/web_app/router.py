from aiohttp import web


async def handle(request):
    text = "Hello"
    return web.Response(text=text)


async def start_app():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()
