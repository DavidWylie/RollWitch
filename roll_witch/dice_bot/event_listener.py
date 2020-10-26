import discord
from . import operation


class EventListenerClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.operations = get_operations()

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

    def get_bot_operation(self, message):
        for prefix, op_getter in self.operations.items():
            if message.content.startswith(prefix):
                operation_input = message.content[len(prefix):]
                return op_getter(roll_string=operation_input, user=message.author.display_name)
        return None


def get_operations():
    token_operation = with_type("token", operation.get_token_roll_operation)
    regex_operation = with_type("regex", operation.get_roll_operation)
    basic_operation = with_type("basic_rpg", operation.get_roll_operation)
    return {
        "!r-t": token_operation,
        "!r-r": regex_operation,
        "!rb": basic_operation,
        "!r-b": basic_operation,
        "!roll": token_operation,
        "!r": token_operation,
    }


def with_type(type, func):
    def op(**kwargs):
        kwargs["roll_type"] = type
        return func(**kwargs)

    return op
