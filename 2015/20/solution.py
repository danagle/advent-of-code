"""
Advent of Code 2015
Day 20: Infinite Elves and Infinite Houses
https://adventofcode.com/2015/day/20
"""
from itertools import chain
from math import sqrt


def read_input_file():
    return int(open("input.txt", "r").read().strip())


def get_divisors(n):
    return set(chain.from_iterable((i, n//i) for i in range(1, int(sqrt(n))+1) if n % i == 0))


def both_parts(target_value):
    part_one = part_two = None
    house = 0
    while part_one is None or part_two is None:
        house += 1
        divisors = get_divisors(house)
        if not part_one and target_value <= sum(divisors) * 10:
            part_one = house
        if not part_two and target_value <= sum(d for d in divisors if house / d <= 50) * 11:
            part_two = house
    print(f"{part_one=}, {part_two=}")


if __name__ == "__main__":
    input_value = read_input_file()
    both_parts(input_value)
