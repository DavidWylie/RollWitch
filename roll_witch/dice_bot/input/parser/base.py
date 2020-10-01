from roll_witch.dice_bot.input.spec import InputPartSpec


class InputParser:
    def __init__(self) -> None:
        super().__init__()
        self.part_specs = {}

    def add_spec(self, spec: InputPartSpec):
        self.part_specs[spec.name] = spec

    def parse(self, roll_string: str):
        raise Exception(f"Unknown Parser")
