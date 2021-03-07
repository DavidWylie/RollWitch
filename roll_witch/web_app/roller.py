import aiohttp_jinja2

from roll_witch.rolling.operation import OperationParser
from aiohttp.web import Request


@aiohttp_jinja2.template("roller.jinja2")
async def roll(request: Request):
    operation_parser = OperationParser()
    data = await request.post()
    author = data["author"]
    try:
        bot_operation = operation_parser.get_command(
            message_content=data["roll_operation"], message_author=author
        )
        if bot_operation:
            operation_output = bot_operation.execute()
            return {"output": operation_output}
    except ValueError:
        return {"output": f" {author}: Invalid Command"}
    except Exception as e:
        if hasattr(e, "message"):
            msg = e.message
        else:
            msg = str(e)
        return {"output": f"I ain't Dead \n  {author}: {msg}"}
