"""
Advent of Code 2016
Day 5: How About a Nice Game of Chess?
https://adventofcode.com/2016/day/5
"""
from hashlib import md5


def read_input_file():
    return open("input.txt", "r").read().strip()


def part_one(door_id):
    password = ""
    index = 0
    while len(password) < 8:
        hex_str = str(md5("{}{}".format(door_id, index).encode("ascii")).hexdigest())
        if "00000" == hex_str[:5]:
            password += hex_str[5]
        index += 1
    return password


def part_two(door_id):
    password = ["_" for _ in range(8)]
    remaining_positions = set("01234567")
    index = 0
    while 0 < len(remaining_positions):
        hex_str = str(md5('{}{}'.format(door_id, index).encode("ascii")).hexdigest())
        if hex_str.startswith("00000") and hex_str[5] in remaining_positions:
            password[int(hex_str[5])] = hex_str[6]
            remaining_positions.remove(hex_str[5])
        index += 1
    return "".join(password)


if __name__ == "__main__":
    id_hash = read_input_file()
    print(part_one(id_hash))
    print(part_two(id_hash))
