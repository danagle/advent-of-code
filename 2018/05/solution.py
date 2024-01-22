"""
Advent of Code 2018
Day 5: Alchemical Reduction
https://adventofcode.com/2018/day/5
"""
from string import ascii_lowercase
from sys import maxsize


def read_input_file():
    return open("input.txt", "r").read().strip()


def react_polymer(polymer_string):
    while True:
        reaction_indexes = []
        for index in range(len(polymer_string) - 1):
            # Check for matching pair of upper and lower case units
            if (polymer_string[index].lower() == polymer_string[index + 1].lower()
                    and polymer_string[index] != polymer_string[index + 1]):
                # Check index is not in the last recorded reaction segment
                if not (reaction_indexes and reaction_indexes[-1] == (index - 1, index + 1)):
                    reaction_indexes.append((index, index + 2))

        if reaction_indexes:
            # Reverse the list of reactions to simplify removing units from polymer
            reaction_indexes.reverse()
            # Remove reactions from polymer string
            for a, b in reaction_indexes:
                polymer_string = polymer_string[:a] + polymer_string[b:]
        else:
            return len(polymer_string)


def part_one(polymer_string):
    return react_polymer(polymer_string)


def part_two(polymer_string):
    shortest_length = maxsize
    for unit in ascii_lowercase:
        # Remove matching units regardless of letter case
        reduced_polymer = "".join(c for c in polymer_string if unit != c.lower())
        reduced_length = react_polymer(reduced_polymer)
        shortest_length = min(shortest_length, reduced_length)
    return shortest_length


if __name__ == "__main__":
    polymer = read_input_file()
    print(part_one(polymer))
    print(part_two(polymer))
