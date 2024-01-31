"""
Advent of Code 2017
Day 9: Stream Processing
https://adventofcode.com/2017/day/7
"""


def read_input_file():
    return open("input.txt", "r").read().strip()


def both_parts(text_stream):
    index = group_score = total_score = non_canceled = 0
    stack, garbage = [], False

    while index < len(text_stream):
        if text_stream[index] == "!":
            index += 1
        elif garbage:
            if text_stream[index] == ">":
                garbage = False
            else:
                non_canceled += 1
        elif text_stream[index] == "{":
            group_score += 1
            stack.append(group_score)
        elif text_stream[index] == "<":
            garbage = True
        elif text_stream[index] == "}":
            group_score -= 1
            total_score += stack.pop()
        index += 1

    return total_score, non_canceled


if __name__ == "__main__":
    text = read_input_file()
    part_one, part_two = both_parts(text)
    print(f"{part_one=}, {part_two=}")
