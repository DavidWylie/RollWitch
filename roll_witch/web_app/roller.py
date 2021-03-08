import aiohttp_jinja2

from aiohttp.web import Request
from roll_witch.rolling import command


@aiohttp_jinja2.template("roller.jinja2")
async def roll(request: Request):
    data = await request.post()
    try:
        bot_operation = command.get_command(
            message_content=data["roll_operation"]
        )
        if bot_operation:
            operation_output = bot_operation.execute()
            return {"output": operation_output}
    except ValueError:
        return {"output": " Invalid Command"}
    except Exception as e:
        if hasattr(e, "message"):
            msg = e.message
        else:
            msg = str(e)
        return {"output": f"I ain't Dead \n {msg}"}
