import os
import discord
from dotenv import load_dotenv
from . import operation


class EventListenerClient(discord.Client):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            print(
                f'{self.user} is connected to the following guild:\n'
                f'{guild.name}(id: {guild.id})'
            )

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('!roll'):
            response = operation.get_roll_operation(message.content[6:], message.author.display_name).execute()
            await message.channel.send(response)
        elif message.content.startswith('!r'):
            response = operation.get_roll_operation(message.content[3:], message.author.display_name).execute()
            await message.channel.send(response)


def start_bot():
    load_dotenv()
    client_token = os.getenv('DISCORD_TOKEN')
    return EventListenerClient().start(client_token)
