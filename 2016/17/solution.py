"""
Advent of Code 2016
Day 17: Two Steps Forward
https://adventofcode.com/2016/day/17
"""
from hashlib import md5
from itertools import compress


def read_input_file():
    """Returns the puzzle input as a string."""
    return open("input.txt", "r").read().strip()


def get_doors_state(initial_text, path_taken):
    bytes_to_hash = (initial_text + "".join(path_taken)).encode("utf-8")
    # "abcdef" is 10-15 in hexadecimal
    return [int(x, 16) > 10 for x in md5(bytes_to_hash).hexdigest()[:4]]


def vaults_breadth_first_search(initial_text):
    start, target = (0, 0), (3, 3)
    vault_directions = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
    queue = [(start, [start], [])]
    while queue:
        (x, y), path_taken, directions = queue.pop(0)
        for direction in compress("UDLR", get_doors_state(initial_text, directions)):
            next_vault = (vault_directions[direction][0] + x, vault_directions[direction][1] + y)
            if 0 <= next_vault[0] < 4 and 0 <= next_vault[1] < 4:
                if target == next_vault:
                    yield directions + [direction]
                else:
                    queue.append((next_vault, path_taken + [next_vault], directions + [direction]))


if __name__ == "__main__":
    puzzle_input = read_input_file()
    vault_paths = list(vaults_breadth_first_search(puzzle_input))
    print("".join(vault_paths[0]), len(vault_paths[-1]))
