from . import RollSpec
from typing import Match
import re


def create_target_spec(target_match: Match):
    return RollSpec(
        dice_count=int(target_match.group(1)),
        dice_sides=int(target_match.group(2)),
        modifier=0,
        target_number=int(target_match.group(3))
    )


def create_modifier_spec(modifier_match: Match):
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


def parse(roll_string):
    spec_regex = {
        'target_spec': re.compile(r"(\d+)d(\d+)\st([\-]*[0-9]+)"),
        'modifier_spec': re.compile(r"(\d+)d(\d+)\s*([+\-])*([0-9]*)")
    }
    matchers = {
        'target_spec': create_target_spec,
        'modifier_spec': create_modifier_spec
    }

    for spec_name, regex in spec_regex.items():
        match = regex.fullmatch(roll_string)
        if match:
            return matchers.get(spec_name)(match)

    raise ValueError("Unknown spec")
