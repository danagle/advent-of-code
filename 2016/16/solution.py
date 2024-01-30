"""
Advent of Code 2016
Day 16: Dragon Checksum
https://adventofcode.com/2016/day/16
"""


def read_input_file():
    return open("input.txt", "r").read().strip()


def dragon_curve(binary_string):
    b = "".join("0" if c == "1" else "1" for c in reversed(binary_string))
    return "{}0{}".format(binary_string, b)


def binary_checksum(binary_string):
    checksum_bits = []
    for a, b in zip(binary_string[::2], binary_string[1::2]):
        checksum_bits.append("1" if a == b else "0")
    if len(checksum_bits) % 2 != 0:
        return "".join(checksum_bits)
    else:
        return binary_checksum("".join(checksum_bits))


def generate_binary_string(binary_str, length):
    while len(binary_str) < length:
        binary_str = dragon_curve(binary_str)
    return binary_str[:length]


def part_one(data):
    return binary_checksum(generate_binary_string(data, 272))


def part_two(data):
    return binary_checksum(generate_binary_string(data, 35651584))


if __name__ == "__main__":
    data = read_input_file()
    print(part_one(data))
    print(part_two(data))
