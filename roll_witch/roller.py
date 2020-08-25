import re
from collections import namedtuple
from random import randint

target_spec = re.compile(r"(\d)d(\d+)\st([\-]*[0-9]+)")
modifier_spec = re.compile(r"(\d)d([0-9]+)\s*[+\-]*([0-9]*)")
RollSpec = namedtuple('RollSpec', ['dice_count', 'dice_sides', 'modifier', 'target_number'])
RollResult = namedtuple('RollResult', ['total', 'rolls', 'spec', 'had_target', 'met_target'])


def roll_percentile(roll_string, user):
    try:
        roll_spec = parse_roll_string(roll_string)
        roll_result = do_roll(roll_spec)
        return write_output(roll_result, user)
    except Exception as e:
        print(f"Error {e}")


def write_output(roll_result: RollResult, user):
    print(f"Roll Result: {roll_result}")
    if roll_result.spec.modifier != 0:
        if roll_result.spec.modifier > 0:
            total_string = f"{roll_result.total} + {roll_result.spec.modifier}"
        else:
            total_string = f"{roll_result.total} {roll_result.spec.modifier}"
    else:
        total_string = f"{roll_result.total}"

    if roll_result.had_target:
        success_string = 'Success' if roll_result.met_target else 'Failed'
        return f"{user} Roll: {total_string} = {roll_result.total} Result: {success_string}"
    else:
        return f"{user} Roll: {total_string} Result: {roll_result.total} "


def do_roll(roll_spec: RollSpec):
    roll_results, roll_total = roll_dice(roll_spec)
    had_target, met_target = check_target(roll_spec, roll_total)

    return RollResult(
        total=roll_total,
        rolls= roll_results,
        spec=roll_spec,
        had_target=had_target,
        met_target=met_target
    )


def check_target(roll_spec, roll_total):
    had_target = roll_spec.target_number is not None
    met_target = False
    if had_target:
        if roll_spec.target_number >= 0:
            met_target = roll_total > roll_spec.target_number
        else:
            met_target = roll_total <= roll_spec.target_number
    return had_target, met_target


def roll_dice(roll_spec):
    roll_results = []
    roll_total = 0
    for dice in range(0, roll_spec.dice_count):
        roll = roll_die(roll_spec)

        roll_results.append(roll)
        roll_total += roll
    roll_total += roll_spec.modifier
    return roll_results, roll_total


def roll_die(roll_spec):
    roll = randint(0, roll_spec.dice_sides)
    if roll == 100 and roll_spec.dice_sides == 100:
        roll = 0

    print(f"rolled: {roll}")
    return roll


def parse_roll_string(roll_string):
    target_match = target_spec.fullmatch(roll_string)
    if target_match:
        print(f"Target Match: {target_match}")
        return RollSpec(
            dice_count=int(target_match.group(1)),
            dice_sides=int(target_match.group(2)),
            modifier=0,
            target_number=int(target_match.group(3))
        )

    modifier_match = modifier_spec.fullmatch(roll_string)
    if modifier_match:
        print(f"Modifier Match: {modifier_match}")
        return RollSpec(
            dice_count=int(modifier_match.group(1)),
            dice_sides=int(modifier_match.group(2)),
            modifier=int(modifier_match.group(3) if modifier_match.group(3) else 0),
            target_number=None
        )
