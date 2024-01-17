"""
Advent of Code 2016
Day 1: No Time for a Taxicab
https://adventofcode.com/2016/day/1
"""


def read_input_file():
    return [(direction[0], int(direction[1:])) for direction in open('input.txt', 'r').read().split(", ")]


def walk_the_blocks(instructions):
    orientation = 0
    position = first_visited_twice = (0, 0)
    moves = ((0, 1), (1, 0), (0, -1), (-1, 0))
    visited = {position}
    has_visited_before = False
    for direction, blocks in instructions:
        # Right turn is clockwise (+), Left turn is counter-clockwise (-)
        orientation = (orientation + (1 if direction == "R" else -1)) % 4
        # Move to new position
        for _ in range(blocks):
            position = tuple(sum(c) for c in (zip(position, moves[orientation])))
            # Part 2
            if not has_visited_before and position in visited:
                first_visited_twice = position
                has_visited_before = True
            else:
                visited.add(position)
    # Calculate Manhattan distances
    return tuple(sum(map(abs, p)) for p in (position, first_visited_twice))


if __name__ == "__main__":
    directions = read_input_file()
    part_one, part_two = walk_the_blocks(directions)
    print(f"{part_one=}, {part_two=}")
