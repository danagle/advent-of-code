"""
Advent of Code 2018
Day 3: No Matter How You Slice It
https://adventofcode.com/2018/day/3
"""
from collections import defaultdict
from re import findall


def read_input_file():
    return [tuple(map(int, findall("(\d+)", line))) for line in open("input.txt", "r").read().splitlines()]


def analyze_fabric_claims(claims):
    fabric_claims = defaultdict(int)
    for claim_id, left, top, width, height in claims:
        for x in range(left, left + width):
            for y in range(top, top + height):
                fabric_claims[(x, y)] += 1
    part_one = sum(1 for count in fabric_claims.values() if count > 1)
    for claim_id, left, top, width, height in claims:
        overlap_detected = False
        for x in range(left, left + width):
            for y in range(top, top + height):
                if fabric_claims[(x, y)] > 1:
                    overlap_detected = True
        if not overlap_detected:
            part_two = claim_id
    print(f"{part_one=}, {part_two=}")


if __name__ == "__main__":
    data = read_input_file()
    analyze_fabric_claims(data)
