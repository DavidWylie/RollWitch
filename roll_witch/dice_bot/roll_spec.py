class RollSpec():
    def __init__(self, dice_count=0, dice_sides=0, modifier=0, target_number=None, operation='+') -> None:
        super().__init__()
        self.dice_count = dice_count
        self.dice_sides = dice_sides
        self.dice_modifier = modifier
        self.target_number = target_number
        self.operation = operation

    def has_target(self) -> bool:
        return self.target_number is not None

    def has_modifier(self) -> bool:
        return self.dice_modifier != 0


class OperationSpec():
    def __init__(self) -> None:
        super().__init__()
        self.parts = []
        self.target_number= None

    def add_part(self, part: RollSpec):
        self.parts.append(part)
        if part.has_target():
            self.target_number = part.target_number

    def has_target(self) -> bool:
        return self.target_number is not None

    def get_part(self) -> RollSpec:
        for part in self.parts:
            yield part
        return None
