"""
Advent of Code 2016
Day 4: Security Through Obscurity
https://adventofcode.com/2016/day/4
"""
from collections import Counter
from string import ascii_lowercase as a_z


def read_input_file():
    return open("input.txt", "r").read().splitlines()


def part_one(rooms_list):
    total = 0
    for room in rooms_list:
        tokens = room.split("-")
        encrypted_name = "".join(tokens[:-1])
        sector_id, room_checksum = tokens[-1].split("[")
        # Create a checksum string from the 5 most frequent letters
        most_frequent_letters = sorted(list(Counter(encrypted_name).items()), key=lambda t: (-t[1], t[0]))[:5]
        checksum_str = "".join([letter for letter, _ in most_frequent_letters])
        # Remove "]" from room_checksum string
        if checksum_str == room_checksum[:-1]:
            total += int(sector_id)
    return total


def part_two(rooms_list):
    north_pole_id = -1
    for room in rooms_list:
        tokens = room.split("-")
        encrypted = " ".join(tokens[:-1])
        sector_id = int(tokens[-1].split("[")[0])
        decrypted = "".join([a_z[(a_z.index(c) + sector_id) % 26] if c in a_z else c for c in encrypted])
        if "north" in decrypted:
            north_pole_id = sector_id
            break
    return north_pole_id


if __name__ == "__main__":
    data = read_input_file()
    print(part_one(data))
    print(part_two(data))
