"""
Advent of Code 2015
Day 10: Elves Look, Elves Say
https://adventofcode.com/2015/day/10
"""


def read_input_file():
    return open("input.txt", "r").read().strip()


def process_string(number_str, times=40):
    for _ in range(times):
        sequence = []
        index = 0
        while index < len(number_str):
            next_index = index + 1
            while next_index < len(number_str) and number_str[next_index] == number_str[index]:
                next_index += 1
            sequence.append(str(next_index - index))
            sequence.append(number_str[index])
            index = next_index
        number_str = "".join(sequence)
    return len(number_str)


def part_one(number_string):
    return process_string(number_string, 40)


def part_two(number_string):
    return process_string(number_string, 50)


if __name__ == "__main__":
    input_str = read_input_file()
    print(part_one(input_str))
    print(part_two(input_str))
