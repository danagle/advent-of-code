"""
Advent of Code 2015
Day 13: Knights of the Dinner Table
https://adventofcode.com/2015/day/13
"""
from collections import defaultdict
from itertools import permutations


def read_input_file():
    happiness_units = defaultdict(dict)
    lines = open("input.txt").read().splitlines()
    for line in lines:
        tokens = line.replace(".", "").split(" ")
        person_1 = tokens[0]
        person_2 = tokens[-1]
        happiness_adjustment = int(tokens[3])
        if "lose" == tokens[2]:
            happiness_adjustment *= -1
        happiness_units[person_1][person_2] = happiness_adjustment
    return happiness_units


def part_one(happiness_units):
    best_happiness = 0
    num_seats = len(happiness_units)
    for arrangement in permutations(happiness_units.keys()):
        arrangement_score = 0
        for i in range(num_seats):
            next_seat = (i + 1) % num_seats
            arrangement_score += happiness_units[arrangement[i]][arrangement[next_seat]]
            arrangement_score += happiness_units[arrangement[next_seat]][arrangement[i]]
        if arrangement_score > best_happiness:
            best_happiness = arrangement_score
    return best_happiness


def part_two(happiness_units):
    # Add a host to the seating plan
    host = "Igor"
    for guest in happiness_units:
        happiness_units[guest][host] = 0
    for guest in list(happiness_units.keys()):
        happiness_units[host][guest] = 0
    # Calculate best score
    return part_one(happiness_units)


if __name__ == "__main__":
    happiness = read_input_file()
    print(part_one(happiness))
    print(part_two(happiness))
