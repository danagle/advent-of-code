"""
Advent of Code 2016
Day 20: Firewall Rules
https://adventofcode.com/2016/day/20
"""


def read_input_file():
    return [tuple(map(int, line.split("-"))) for line in open("input.txt", "r").read().splitlines()]


def unblocked_ips(blocked_ranges):
    blacklisted = sorted(blocked_ranges, key=lambda r: r[0])
    unblocked_addresses = set()
    address = 0
    while address < 4294967295:
        blocked = False
        for blocked_range in blacklisted:
            if blocked_range[0] <= address <= blocked_range[1]:
                address = blocked_range[1]
                blocked = True
                break
        if not blocked:
            unblocked_addresses.add(address)
        address += 1
    return min(unblocked_addresses), len(unblocked_addresses)


if __name__ == "__main__":
    ip_addresses = read_input_file()
    part_one, part_two = unblocked_ips(ip_addresses)
    print(f"{part_one=}, {part_two=}")
