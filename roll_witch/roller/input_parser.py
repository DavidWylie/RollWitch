from . import RollSpec
import re


target_spec = re.compile(r"(\d+)d(\d+)\st([\-]*[0-9]+)")
modifier_spec = re.compile(r"(\d+)d(\d+)\s*([+\-])*([0-9]*)")


def parse(roll_string):
    target_match = target_spec.fullmatch(roll_string)
    if target_match:
        return RollSpec(
            dice_count=int(target_match.group(1)),
            dice_sides=int(target_match.group(2)),
            modifier=0,
            target_number=int(target_match.group(3))
        )

    modifier_match = modifier_spec.fullmatch(roll_string)

    if modifier_match:
        if modifier_match.group(3):
            if modifier_match.group(3) == '+':
                modifier = int(modifier_match.group(4))
            else:
                modifier = -int(modifier_match.group(4))
        else:
            modifier = 0

        return RollSpec(
            dice_count=int(modifier_match.group(1)),
            dice_sides=int(modifier_match.group(2)),
            modifier=modifier,
            target_number=None
        )
