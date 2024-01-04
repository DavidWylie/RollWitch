from aiohttp import web
import aiohttp_jinja2
import jinja2
from . import roller
import os


@aiohttp_jinja2.template("roller.jinja2")
async def handle_roller(request):
    return {"output": None}


async def warmup(request):
    return web.Response()


async def start_app():
    app = web.Application()

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "templates")
    staticfiles = os.path.join(dirname, "static")
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(filename))

    app.router.add_get("/", handle_roller)
    app.router.add_post("/roll", roller.roll)
    app.router.add_get("/roll", handle_roller)
    app.router.add_get("/_ah/warmup", warmup)
    app.router.add_static("/static", staticfiles)
    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()
