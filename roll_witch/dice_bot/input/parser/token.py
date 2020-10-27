from roll_witch.dice_bot.input.parser.base import InputParser
from roll_witch.dice_bot.spec import OperationSpec


class TokenInputParser(InputParser):
    def parse(self, roll_string: str):
        parts = self.sanitise_operators(roll_string).split()
        spec = OperationSpec()
        for part in parts:
            part_spec = self.parse_part(part)
            spec.add_part(part_spec)
        return spec

    def sanitise_operators(self, roll_string) -> str:
        sanitized_string = self._sanitize_operator("+", roll_string)
        sanitized_string = self._sanitize_operator("-", sanitized_string)
        sanitized_string = self._sanitize_operator("*", sanitized_string)
        return sanitized_string

    def _sanitize_operator(self, operator, string):
        return (
            string.replace(f" {operator} ", operator)
            .replace(operator, f" {operator}")
            .replace(f"t {operator}", f"t{operator}")
        )

    def parse_part(self, part_string):
        for spec_name, spec in self.part_specs.items():
            match = spec.matches_pattern(part_string)
            if match:
                return spec.apply(match)
        raise Exception(
            f"Roll What?  {part_string} is not valid Try again  e.g. roll 1d10 +10 or roll 1d6 t6"
        )
