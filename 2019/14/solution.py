"""
Advent of Code 2019
Day 14: Space Stoichiometry
https://adventofcode.com/2019/day/14
"""
from math import ceil


def read_input_file():
    element_reactions = {}

    def parse_element_volume(element_string):
        volume, element = element_string.strip().split()
        return element, int(volume)

    for line in open("input.txt", "r").read().splitlines():
        left, right = line.split(" => ")
        left, right = list(map(parse_element_volume, left.split(","))), parse_element_volume(right)
        element_reactions[right[0]] = (right[1], left)

    return element_reactions


def stocked_inventory(reactions, inventory, element, amount_needed):
    if inventory[element] >= amount_needed:
        return True
    if element == "ORE":
        return False
    number_required = ceil((amount_needed - inventory[element]) / reactions[element][0])
    stocked = True
    for sub_element, sub_amount_needed in reactions[element][1]:
        stocked = stocked and stocked_inventory(reactions, inventory, sub_element, number_required * sub_amount_needed)
        inventory[sub_element] -= number_required * sub_amount_needed
    if stocked:
        inventory[element] += number_required * reactions[element][0]
    return stocked


def part_one(reactions):
    low, high = 0, 10**12
    while low < high:
        mid = low + (high - low) // 2
        inventory_stock = {element: 0 for element in reactions}
        inventory_stock["ORE"] = mid
        if stocked_inventory(reactions, inventory_stock, "FUEL", 1):
            high = mid
        else:
            low = mid + 1
    return low


def part_two(reactions):
    low, high, inventory_stock = 0, 10**12, {}
    while low < high-1:
        mid = low + (high - low) // 2
        inventory_stock = {element: 0 for element in reactions}
        inventory_stock["ORE"] = 10**12
        if stocked_inventory(reactions, inventory_stock, "FUEL", mid):
            low = mid
        else:
            high = mid - 1
    return high if stocked_inventory(reactions, inventory_stock, "FUEL", high) else low


if __name__ == "__main__":
    fuel_reactions = read_input_file()
    print(f"part_one: {part_one(fuel_reactions)}")
    print(f"part_two: {part_two(fuel_reactions)}")
