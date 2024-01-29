"""
Advent of Code 2015
Day 11: Corporate Policy
https://adventofcode.com/2015/day/11
"""
from string import ascii_lowercase


def read_input_file():
    return open("input.txt", "r").read().strip()


def next_possible_password(text_str):
    shifted_chars = {}
    chars = "".join([char for char in ascii_lowercase if char not in {"i", "o", "l"}])
    for i in range(len(chars) - 1):
        shifted_chars[chars[i]] = chars[i + 1]
    in_progress_str = list(reversed(text_str))
    while True:
        index = 0
        while True:
            if in_progress_str[index] == "z":
                in_progress_str[index] = "a"
            else:
                in_progress_str[index] = shifted_chars[in_progress_str[index]]
                break
            index += 1
        yield "".join(reversed(in_progress_str))


def check_rules(text_str):
    # May not contain the letters i, o, or l
    if any(c in text_str for c in {"i", "l", "o"}):
        return False
    # Must include one increasing straight of at least three letters
    found_straight = False
    for i in range(len(ascii_lowercase) - 2):
        if ascii_lowercase[i:i + 3] in text_str:
            found_straight = True
            break
    if not found_straight:
        return False
    # Must contain at least two different, non-overlapping pairs of letters
    pairs = 0
    for c in ascii_lowercase:
        if c * 2 in text_str:
            pairs += 1
    return pairs >= 2


def get_next_password(password):
    for candidate in next_possible_password(password):
        if check_rules(candidate):
            return candidate


if __name__ == "__main__":
    input_text = read_input_file()
    part_one = get_next_password(input_text)
    part_two = get_next_password(part_one)
    print(f"{part_one=}, {part_two=}")
