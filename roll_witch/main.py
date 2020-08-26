from roll_witch import bot
from aiohttp import web
import asyncio
from dotenv import load_dotenv
import os

async def handle(request):
    text = "Hello"
    return web.Response(text=text)

async def start_app():
    load_dotenv()
    PORT = os.getenv('PORT')
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', PORT)
    await site.start()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    loop.run_until_complete(start_app())
    loop.run_until_complete(bot.start_bot())
    try:
        loop.run_forever()
    finally:
        loop.close()
