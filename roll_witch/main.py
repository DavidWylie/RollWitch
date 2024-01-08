import os

from roll_witch.dice_bot import bot
from roll_witch.web_app import router
import asyncio

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    loop.run_until_complete(router.start_app())
    if os.getenv("DISABLE_BOT") == "true":
        print("Bot is disabled")
    else:
        loop.run_until_complete(bot.start_bot())
    try:
        loop.run_forever()
    finally:
        loop.close()
