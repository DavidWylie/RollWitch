import discord
from roll_witch.rolling.command import get_command


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
            command, roll_string = get_command(message_content=message.content)
            if command:
                response = command.execute(
                    roll_string=roll_string,
                    user=message.author.display_name,
                )
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
