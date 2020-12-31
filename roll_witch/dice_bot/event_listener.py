import discord
from .operation import OperationParser


class EventListenerClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.operation_parser = OperationParser()

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
            bot_operation = self.operation_parser.parse_operation(message)
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
