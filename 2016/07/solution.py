"""
Advent of Code 2016
Day 7: Internet Protocol Version 7
https://adventofcode.com/2016/day/7
"""
from re import compile, findall, search, sub


def read_input_file():
    return open("input.txt", "r").read().splitlines()


def part_one(data):
    total = 0
    abba_regex = compile(r"(\w)(?!\1)(\w)\2\1")
    for address in data:
        if abba_regex.search(address):
            is_tls = True
            hypernet_sequences = findall(r"\[[^\]]*\]", address)
            for found in hypernet_sequences:
                if abba_regex.search(found):
                    is_tls = False
                    break
            if is_tls:
                total += 1
    return total


def incremental_regex_search(regex, text):
    search_results = []
    hay_stack = text
    while len(hay_stack):
        m = search(regex, hay_stack)
        if m:
            search_results.append(m.group())
            hay_stack = hay_stack[m.start() + 1:]
        else:
            break
    return search_results


def part_two(data):
    total = 0
    bab_regex = compile(r"(\w)(?!\1)(\w)\1")
    for address in data:
        supernet_str = sub(r"\[.*?\]", "", address)
        hypernet_str = "".join(findall(r"\[+(.*?)\]", address))
        bab_pairs = set([t[:2] for t in incremental_regex_search(bab_regex, hypernet_str)])
        aba_pairs = set([t[1:] for t in incremental_regex_search(bab_regex, supernet_str)])
        if aba_pairs.intersection(bab_pairs):
            total += 1
    return total


if __name__ == "__main__":
    addresses = read_input_file()
    print(f"Part 1: {part_one(addresses)} TLS addresses.")
    print(f"Part 2: {part_two(addresses)} SSL addresses.")
