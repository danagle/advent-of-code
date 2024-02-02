"""
Advent of Code 2017
Day 19: A Series of Tube
https://adventofcode.com/2017/day/19
"""
from string import ascii_uppercase


def read_input_file():
    return [[c for c in line] for line in open("input.txt", "r").read().splitlines()]


def both_part(diagram):
    sequence, steps, direction = [], 0, 0
    position = (0, diagram[0].index("|"))
    moves = ((1, 0), (0, -1), (-1, 0), (0, 1))

    while True:
        tile = diagram[position[0]][position[1]]
        if " " == tile:
            break
        elif tile.isalpha():
            sequence.append(tile)
        elif "+" == tile:
            for index, move in enumerate(moves):
                if index == (direction + 2) % len(moves):
                    continue
                if diagram[position[0] + move[0]][position[1] + move[1]] != " ":
                    direction = index
                    break

        steps += 1
        position = (position[0] + moves[direction][0], position[1] + moves[direction][1])

    return "".join(sequence), steps


if __name__ == "__main__":
    routing_diagram = read_input_file()
    part_one, part_two = both_part(routing_diagram)
    print(f"{part_one=}, {part_two=}")
