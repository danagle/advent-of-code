"""
Advent of Code 2015
Day 16: Aunt Sue
https://adventofcode.com/2015/day/16
"""
from collections import defaultdict


def read_input_file():
    aunt_sues = defaultdict(dict)
    lines = open("input.txt", "r").read().splitlines()
    for line in lines:
        tokens = line.replace(":", "").replace("," , "").split(" ")
        for i in range(2, len(tokens), 2):
            aunt_sues[tokens[1]][tokens[i]] = int(tokens[i+1])
    return aunt_sues


def part_one(aunts, tape):
    number = -1
    for number in aunts:
        if all(aunts[number].get(compound, value) == value for compound, value in tape.items()):
            break
    return number


def part_two(aunts, tape):
    number, greater_than, fewer_than = -1, {"cats", "trees"}, {"pomeranians", "goldfish"}
    others = tuple([c for c in tape if c not in {"cats", "trees", "pomeranians", "goldfish"}])
    for number in aunts:
        aunt = aunts[number]
        if all(aunt.get(c, tape[c]+1) > tape[c] for c in greater_than) and \
                all(aunt.get(c, tape[c]-1) < tape[c] for c in fewer_than) and \
                all(aunt.get(c, tape[c]) == tape[c] for c in others):
            break
    return number


if __name__ == "__main__":
    ticker_tape = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }
    aunt_sue_collection = read_input_file()
    print(part_one(aunt_sue_collection, ticker_tape))
    print(part_two(aunt_sue_collection, ticker_tape))
