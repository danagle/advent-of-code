"""
Advent of Code 2018
Day 20: A Regular Map
https://adventofcode.com/2018/day/20
"""
from collections import defaultdict


def read_input_file():
    return open("input.txt", "r").read().strip()


def both_parts(input_data):
    directions = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}
    prev_x = prev_y = x, y = 5000, 5000
    positions = []
    maze, distances = defaultdict(set), defaultdict(int)

    for c in input_data[1:-1]:
        if c == "(":
            positions.append((x, y))
        elif c == ")":
            x, y = positions.pop()
        elif c == "|":
            x, y = positions[-1]
        else:
            dx, dy = directions[c]
            x, y = x + dx, y + dy
            maze[(x, y)].add((prev_x, prev_y))
            if distances[(x, y)] != 0:
                distances[(x, y)] = min(distances[(x, y)], distances[(prev_x, prev_y)] + 1)
            else:
                distances[(x, y)] = distances[(prev_x, prev_y)] + 1
        prev_x, prev_y = x, y

    return max(distances.values()), len([x for x in distances.values() if x >= 1000])


if __name__ == "__main__":
    input_data = read_input_file()
    part_one, part_two = both_parts(input_data)
    print(f"{part_one=}, {part_two=}")
