"""
Advent of Code 2017
Day 4: High-Entropy Passphrases
https://adventofcode.com/2017/day/4
"""


def read_input_file():
    return [line.split(" ") for line in open("input.txt", "r").read().splitlines()]


def part_one(passphrases):
    return sum([len(set(words)) == len(words) for words in passphrases])


def part_two(passphrases):
    return sum([len(set(["".join(sorted(list(word))) for word in words])) == len(words) for words in passphrases])


if __name__ == "__main__":
    data = read_input_file()
    print(part_one(data))
    print(part_two(data))
