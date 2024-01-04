import aiohttp_jinja2

from aiohttp.web import Request
from roll_witch.rolling import command


@aiohttp_jinja2.template("roller.jinja2")
async def roll(request: Request):
    data = await request.post()
    try:
        roll_operation = data['roll_operation']
        if not(roll_operation.startswith('!r')):
            roll_operation = f"!r {roll_operation}"

        bot_operation, roll_string = command.get_command(
            message_content=roll_operation
        )
        print(f"Roll Request: {roll_string}")
        if bot_operation:
            operation_output = bot_operation.execute(
                roll_string=roll_string,
                user='',
            )
            print(f"Output: {operation_output}")
            return {
                "output": {
                    "roll_request": roll_string,
                    "roll_result": operation_output,
                }
            }
    except ValueError:
        return {
            "output": {
                "error": "Invalid Command",
                "roll_request": data['roll_operation'],
                "roll_result": "Error"
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
                "roll_request": data['roll_operation'],
                "roll_result": "Error"
            }
        }
