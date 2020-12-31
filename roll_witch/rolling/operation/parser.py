from .factory import standard_factory, token_factory


def _with_type(type, func):
    def op(**kwargs):
        kwargs["roll_type"] = type
        return func(**kwargs)

    return op


class OperationParser:
    def __init__(self):
        token_operation = _with_type("token", token_factory.get_roll_operation)
        regex_operation = _with_type("regex", standard_factory.get_roll_operation)
        basic_operation = _with_type("basic_rpg", standard_factory.get_roll_operation)
        self.operations = {
            "!r-t": token_operation,
            "!r-r": regex_operation,
            "!rb": basic_operation,
            "!r-b": basic_operation,
            "!roll": token_operation,
            "!r": token_operation,
        }

    def parse_operation(self, message_content, message_author):
        for prefix, op_getter in self.operations.items():
            if message_content.startswith(prefix):
                operation_input = message_content[len(prefix):].lstrip()
                return op_getter(roll_string=operation_input, user=message_author)
        return None
