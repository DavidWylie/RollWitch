from .basic import BasicOperation
from .regex import RegexOperation
from .shadow_run import ShadowRunOperation
from .token import TokenOperation

operations = {
    "!r-t": TokenOperation(),
    "!r-r": RegexOperation(),
    "!rb": BasicOperation(),
    "!r-b": BasicOperation(),
    "!roll": TokenOperation(),
    "!r": TokenOperation(),
    "!sr": ShadowRunOperation(),
}


def clean_command(command_string):
    return command_string.lower().replace("! ", "!").lstrip()


def remove_prefix(command_string, prefix):
    if command_string.startswith(prefix):
        return command_string[len(prefix):]
    return command_string.lstrip()


def get_command(message_content: str):
    clean_command_string = clean_command(message_content)
    for prefix, op_getter in operations.items():
        if clean_command_string.startswith(prefix):
            operation_input = remove_prefix(clean_command_string, prefix)
            return op_getter, operation_input
    return None, message_content
