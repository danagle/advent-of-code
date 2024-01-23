"""
Advent of Code 2019
Day 4: Secure Container
https://adventofcode.com/2019/day/4
"""


def read_input_file():
    return tuple(map(int, open("input.txt", "r").read().strip().split("-")))


def password_criteria(password, part2=False):
    if any(password[i] > password[i+1] for i in range(5)):
        return False
    groups = [password.count(digit) for digit in set(password)]
    if not part2:
        result = any(group >= 2 for group in groups)
    else:
        result = any(group == 2 for group in groups)
    return result


def part_one(range_values):
    a, b = range_values
    return sum(password_criteria(str(number)) for number in range(a, b + 1))


def part_two(range_values):
    a, b = range_values
    return sum(password_criteria(str(number), True) for number in range(a, b + 1))


if __name__ == "__main__":
    values = read_input_file()
    print(part_one(values))
    print(part_two(values))
