from . import basic, token, regex, shadow_run

operations = {
    "!r-t": token,
    "!r-r": regex,
    "!rb": basic,
    "!r-b": basic,
    "!roll": token,
    "!r": token,
    "!sr": shadow_run
}


def clean_command(command_string):
    return command_string.lower().replace("! ", "!").lstrip()


def get_command(message_content: str):
    clean_command_string = clean_command(message_content)
    for prefix, op_getter in operations.items():
        if clean_command_string.startswith(prefix):
            operation_input = clean_command_string[len(prefix):].lstrip()
            return op_getter, operation_input
    return None, message_content
