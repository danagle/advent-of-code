"""
Advent of Code 2015
Day 12: JSAbacusFramework.io
https://adventofcode.com/2015/day/12
"""
from json import loads as load_json_string
from re import findall


def read_input_file():
    return open("input.txt", "r").read().strip()


def part_one(text):
    return sum(list(map(int, findall(r"-?\d+", text))))


def filtered_out_red(elem):
    numbers = []
    if isinstance(elem, int):
        numbers.append(elem)
    elif isinstance(elem, list):
        for item in elem:
            numbers.extend(filtered_out_red(item))
    elif isinstance(elem, dict):
        # Ignore any object (and all of its children) which has any property with the value "red"
        if "red" not in elem.values():
            for item in elem.values():
                numbers.extend(filtered_out_red(item))
    return numbers


def part_two(text):
    input_json = load_json_string(text)
    return sum(filtered_out_red(input_json))


if __name__ == "__main__":
    input_text = read_input_file()
    print(part_one(input_text))
    print(part_two(input_text))
