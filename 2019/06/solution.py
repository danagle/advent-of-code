"""
Advent of Code 2019
Day 6: Universal Orbit Map
https://adventofcode.com/2019/day/6
"""
from re import search as regex_search


def read_input_file():
    orbits = [regex_search(r"(.*)\)(.*)", line).groups() for line in open("input.txt", "r").read().splitlines()]
    return {orbit[0]: [o[1] for o in orbits if o[0] == orbit[0]] for orbit in orbits}


def part_one(orbits):

    def count_orbits(o):
        nonlocal orbits
        return len(orbits.get(o, [])) + sum((count_orbits(_) for _ in orbits.get(o, [])))

    return sum(count_orbits(o) for o in orbits)


def part_two(orbits):
    swapped = dict((v, k) for k, values in orbits.items() for v in values)

    def get_all_orbits(body):
        nonlocal swapped
        all_orbits = []
        current = body
        while current != "COM":
            current = swapped.get(current)
            all_orbits.append(current)
        return all_orbits

    def orbital_transfer_count(a, b):
        a_orbits = get_all_orbits(a)
        b_orbits = get_all_orbits(b)
        for orbit in a_orbits:
            if orbit in b_orbits:
                return a_orbits.index(orbit) + b_orbits.index(orbit)
        return -1

    return orbital_transfer_count("YOU", "SAN")


if __name__ == "__main__":
    orbits_map = read_input_file()
    print(part_one(orbits_map))
    print(part_two(orbits_map))
