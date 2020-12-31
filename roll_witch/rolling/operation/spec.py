from roll_witch.rolling.roller import RollSpec


class OperationSpec:
    def __init__(self) -> None:
        super().__init__()
        self.parts = []
        self.dice_count = 0
        self.target_number = None

    def add_part(self, part: RollSpec):
        self.parts.append(part)
        self.dice_count += part.dice_count
        if part.has_target():
            self.target_number = part.target_number

    def has_target(self) -> bool:
        return self.target_number is not None
