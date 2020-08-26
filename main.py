import os

import discord
from dotenv import load_dotenv
from roll_witch import roller


import datetime

from flask import Flask, render_template

app = Flask(__name__)



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@app.route('/')
def root():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.
    dummy_times = [datetime.datetime(2018, 1, 1, 10, 0, 0),
                   datetime.datetime(2018, 1, 2, 10, 30, 0),
                   datetime.datetime(2018, 1, 3, 11, 0, 0),
                   ]

    return render_template('index.html', times=dummy_times)

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
    app.run(host='127.0.0.1', port=8080, debug=True)
