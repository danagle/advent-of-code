"""
Advent of Code 2015
Day 19: Medicine for Rudolph
https://adventofcode.com/2015/day/19
"""
from collections import defaultdict
from re import sub


def read_input_file():
    rules_text, molecule_string = open("input.txt").read().split("\n\n")
    rules_dict = defaultdict(list)
    for rule in rules_text.splitlines():
        left, right = rule.split(" => ")
        rules_dict[left].append(right)
    return rules_dict, molecule_string.strip()


def part_one(replacement_rules, molecule):
    distinct_molecules = set()
    for rule, replacements in replacement_rules.items():
        last_index = 0
        while True:
            index = molecule.find(rule, last_index)
            if index == -1:
                break
            for replacement in replacements:
                distinct_molecules.add(molecule[:index] + replacement + molecule[index+len(rule):])
            last_index = index + len(rule)
    return len(distinct_molecules)


def part_two(replacement_rules, molecule):
    reversed_rules = {v[::-1]: k[::-1]
                      for k, chemicals in replacement_rules.items()
                      for v in chemicals}
    reversed_molecule = molecule[::-1]
    regex_pattern = "|".join(reversed_rules.keys())
    replacement_count = 0

    def replace_match(match):
        nonlocal reversed_rules
        return reversed_rules[match.group()]

    while "e" != reversed_molecule:
        reversed_molecule = sub(regex_pattern, replace_match, reversed_molecule, 1)
        replacement_count += 1
    return replacement_count


if __name__ == "__main__":
    rules, medicine = read_input_file()
    print(part_one(rules, medicine))
    print(part_two(rules, medicine))
