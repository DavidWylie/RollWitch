import os

import discord
from dotenv import load_dotenv
from roll_witch import roller

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!roll'):
        response = roller.roll_percentile(message.content[6:], message.author.display_name)
        await message.channel.send(response)
    elif message.content.startswith('!r'):
        response = roller.roll_percentile(message.content[3:], message.author.display_name)
        await message.channel.send(response)


if __name__ == '__main__':
    client.run(TOKEN)
