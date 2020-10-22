import os
import discord
from dotenv import load_dotenv
from . import operation


class EventListenerClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print(f"{self.user} has connected to Discord!")
        for guild in self.guilds:
            print(
                f"{self.user} is connected to the following guild:\n"
                f"{guild.name}(id: {guild.id})"
            )

    async def on_message(self, message):
        if message.author == self.user:
            return
        try:
            bot_operation = self.get_bot_operation(message)
            if bot_operation:
                response = bot_operation.execute()
                await message.channel.send(response)
        except ValueError:
            await message.channel.send(
                f" {message.author.display_name}: Invalid Command"
            )
        except Exception as e:
            if hasattr(e, "message"):
                msg = e.message
            else:
                msg = str(e)
            await message.channel.send(
                f"I ain't Dead \n  {message.author.display_name}: {msg}"
            )

    @staticmethod
    def get_bot_operation(message):
        bot_operation = None
        operations = {
            "!r-t": operation.get_token_roll_operation,
            "!r-r": operation.get_roll_operation,
            "!roll": operation.get_token_roll_operation,
            "!r": operation.get_token_roll_operation,
        }
        for prefix, operation_getter in operations.items():
            if message.content.startswith(prefix):
                operation_input = message.content[len(prefix):]
                return operation_getter(operation_input, message.author.display_name)

        return bot_operation


def start_bot():
    load_dotenv()
    client_token = os.getenv("DISCORD_TOKEN")
    return EventListenerClient().start(client_token)
