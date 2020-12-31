from roll_witch.rolling.operation import OperationParser
from aiohttp.web import Request, Response


def roll(request: Request):
    operation_parser = OperationParser()
    data = await request.post()
    bot_operation = operation_parser.parse_operation(
        message_content=data["roll_operation"], message_author=data["author"]
    )
    if bot_operation:
        operation_output = bot_operation.execute()
        return Response(body=operation_output)
    else:
        return Response(body="Unknown operation")
