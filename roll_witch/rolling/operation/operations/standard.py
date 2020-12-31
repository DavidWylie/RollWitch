from roll_witch.rolling.roller import RollSpec
from roll_witch.rolling.protocols import Operation


class RollOperation(Operation):
    def __init__(self, spec: RollSpec, user: str, roller, output) -> None:
        super().__init__()
        self.user = user
        self.spec = spec
        self.roller = roller
        self.output = output

    def execute(self):
        try:
            roll_result = self.roller.roll(self.spec)
            output = self.output.write_output(roll_result, self.user)
            if len(output) > 2000:
                raise ValueError()
            return output
        except ValueError:
            raise Exception("Your answer is just too big to give you")
        except Exception as e:
            raise Exception(f"{e}")
