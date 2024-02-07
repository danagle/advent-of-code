"""
Advent of Code 2018
Day 18: Settlers of The North Pole
https://adventofcode.com/2018/day/18
"""
from collections import defaultdict
from itertools import count, product
from numpy import array, count_nonzero, uint8


def read_input_file():
    return array([[".|#".index(c) for c in r] for r in open("input.txt", "r").read().splitlines()], dtype=uint8)


def both_parts(scan):
    resource_values = defaultdict(set, {})

    def adjacent_count(i, j, resource):
        nonlocal scan
        return count_nonzero(scan[max(0, i-1):i+2, max(0, j-1):j+2] == resource)

    for minute in count(1):
        new_scan = scan.copy()
        for x, y in product(range(50), range(50)):
            trees = adjacent_count(x, y, 1)
            lumberyards = adjacent_count(x, y, 2)
            if 0 == scan[x, y] and trees >= 3:
                new_scan[x, y] = 1
            elif 1 == scan[x, y] and lumberyards >= 3:
                new_scan[x, y] = 2
            elif 2 == scan[x, y] and (lumberyards < 2 or trees == 0):
                new_scan[x, y] = 0
        scan = new_scan
        value = count_nonzero(scan == 2) * count_nonzero(scan == 1)
        if 10 == minute:
            print("Part 1:",  value)
        if value in resource_values and len(resource_values[value]) > 3:
            divisor = minute - sorted(resource_values[value])[-1]
            if minute % divisor == 1_000_000_000 % divisor:
                print("Part 2:", value)
                break
        resource_values[value].add(minute)


if __name__ == "__main__":
    area_scan = read_input_file()
    both_parts(area_scan)
