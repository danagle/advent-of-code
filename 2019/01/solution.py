"""
Advent of Code 2019
Day 1: The Tyranny of the Rocket Equation
https://adventofcode.com/2019/day/1
"""


def read_input_file():
    return [int(line) for line in open("input.txt", "r").read().splitlines()]


def part_one(data):
    return sum(mass // 3 - 2 for mass in data)


def rocket_equation_double_checker(fuel_mass):
    next_fuel_mass = fuel_mass // 3 - 2
    if next_fuel_mass < 0:
        return 0
    return next_fuel_mass + rocket_equation_double_checker(next_fuel_mass)


def part_two(data):
    total_fuel_required = 0
    for module_mass in data:
        fuel_mass = module_mass // 3 - 2
        total_fuel_required += fuel_mass + rocket_equation_double_checker(fuel_mass)
    return total_fuel_required


if __name__ == "__main__":
    masses_list = read_input_file()
    print(part_one(masses_list))
    print(part_two(masses_list))
