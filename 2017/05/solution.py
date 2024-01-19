"""
Advent of Code 2017
Day 5: A Maze of Twisty Trampolines, All Alike
https://adventofcode.com/2017/day/5
"""


def read_input_file():
    return [int(line) for line in open("input.txt", "r").read().splitlines()]


def follow_jump_instructions(offsets_list, part2=False):
    position = 0
    jumps = 0
    while position < len(offsets_list):
        offset = offsets_list[position]
        if part2 and 3 <= offset:
            offsets_list[position] -= 1
        else:
            offsets_list[position] += 1
        jumps += 1
        position += offset
    return jumps


if __name__ == "__main__":
    data = read_input_file()
    print(follow_jump_instructions(data.copy()))
    print(follow_jump_instructions(data.copy(), True))
