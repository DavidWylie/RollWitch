import aiohttp_jinja2

from aiohttp.web import Request
from roll_witch.rolling import command
from roll_witch.rolling.output.web_operation import WebOperationOutputWriter


@aiohttp_jinja2.template("roller.jinja2")
async def roll(request: Request):
    data = await request.post()
    try:
        roll_type = data["roll_type"]
        roll_target = f"t{data["roll_target"]}" if data["roll_target"] else ""
        roll_operation = f"{roll_type} {data["roll_operation"]} {roll_target}"
        bot_operation, roll_string = command.get_command(message_content=roll_operation)

        print(f"Roll Request: {roll_string}")
        if bot_operation:
            operation_output = bot_operation.execute(
                roll_string=roll_string,
                user="",
            )
            output_formatter = WebOperationOutputWriter()
            output = output_formatter.write_output(
                operation_request=roll_string,
                result=operation_output,
                roller=bot_operation.name,
            )
            print(f"Output: {output}")
            return {
                "output": output,
            }
    except ValueError:
        return {
            "output": {
                "error": "Invalid Command",
                "roll_request": data["roll_operation"],
                "roll_result": "Error",
            }
        }
    except Exception as e:
        if hasattr(e, "message"):
            msg = e.message
        else:
            msg = str(e)
        return {
            "output": {
                "error": msg,
                "roll_request": data["roll_operation"],
                "roll_result": "Error",
            }
        }
