"""
Advent of Code 2015
Day 5: Doesn't He Have Intern-Elves For This?
https://adventofcode.com/2015/day/5
"""


def read_input_file():
    return [line for line in open("input.txt", "r").read().splitlines()]


def part_one(lines):
    nice_lines = 0
    naughty_strings = ("ab", "cd", "pq", "xy")
    for line in lines:
        three_vowels = 2 < sum([*map(line.lower().count, "aeiou")])
        double_letters = any(set(enumerate(line)) & set(enumerate(line, 1)))
        naughty_check = not any(pair in line for pair in naughty_strings)
        if three_vowels and double_letters and naughty_check:
            nice_lines += 1
    return nice_lines


def part_two(lines):
    nice_lines = 0
    for line in lines:
        repeats = 0
        for i in range(len(line) - 2):
            if line[i] == line[i + 2]:
                repeats += 1
        pairs = 0
        for i in range(len(line) - 1):
            for j in range(i + 2, len(line) - 1):
                if line[i:i + 2] == line[j:j + 2]:
                    pairs += 1
        if repeats and pairs:
            nice_lines += 1

    return nice_lines


if __name__ == "__main__":
    strings = read_input_file()
    print(part_one(strings))
    print(part_two(strings))
