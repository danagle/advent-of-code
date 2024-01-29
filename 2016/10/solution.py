"""
Advent of Code 2016
Day 10: Balance Bots
https://adventofcode.com/2016/day/10
"""
from collections import defaultdict
from math import prod


def read_input_file():
    commands = []
    for line in open("input.txt", "r").read().splitlines():
        line = line.split(" ")
        if "value" == line[0]:
            commands.append(("value", (int(line[1]), int(line[5]))))
        else:
            commands.append(("give", (int(line[1]), line[5], int(line[6]), line[10], int(line[11]))))
    return commands


def follow_instructions(commands):
    outputs = defaultdict(list)
    bots = defaultdict(list)
    part_one = -1

    for command, params in commands:
        if "value" == command:
            value, bot_id = params
            bots[bot_id].append(value)

    processing = True
    while processing:
        processing = False
        for command, params in commands:
            if "give" == command:
                bot_id, low_target, low_id, high_target, high_id = params
                if len(bots[bot_id]) == 2:
                    processing = True
                    low_value, high_value = sorted(bots[bot_id])
                    if (low_value, high_value) == (17, 61):
                        part_one = bot_id
                    bots[bot_id] = []
                    if low_target == "bot":
                        bots[low_id].append(low_value)
                    else:
                        outputs[low_id].append(low_value)
                    if high_target == "bot":
                        bots[high_id].append(high_value)
                    else:
                        outputs[high_id].append(high_value)
    part_two = prod(outputs[i][0] for i in range(3))
    print(f"{part_one=}, {part_two=}")


if __name__ == "__main__":
    data = read_input_file()
    follow_instructions(data)
