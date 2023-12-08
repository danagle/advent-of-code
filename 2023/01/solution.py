import re


def text_to_digit(text_line):
    digit_strings = {"one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    indexes = dict()
    digit_string_present = True
    while digit_string_present:
        for digit_string in digit_strings.keys():
            indexes[digit_string] = text_line.find(digit_string)
        first_index = None
        first_digit = None
        for digit_key in indexes.keys():
            digit_index = None
            if indexes[digit_key] > -1:
                digit_index = indexes[digit_key]
            if (first_index is None) or (digit_index is not None and digit_index < first_index):
                first_index = digit_index
                first_digit = digit_key
        if first_index is not None:
            text_line = text_line.replace(first_digit, digit_strings[first_digit])
        else:
            digit_string_present = False

    return text_line


def text_to_digits(text_line):
    digit_strings = (
        ("one",'1'),
        ("two",'2'),
        ("three",'3'),
        ("four",'4'),
        ("five",'5'),
        ("six",'6'),
        ("seven",'7'),
        ("eight",'8'),
        ("nine",'9')
    )
    reversed_text = reverse_text_string(text_line)
    indexes = [(text_line.find(digit_string), reversed_text.find(reverse_text_string(digit_string)))
               for digit_string, _ in digit_strings]
    for index, index_tuple in enumerate(indexes):
        digit = str(index + 1)
        a, b = index_tuple
        if b > -1:
            b = len(text_line) - b
            text_line = text_line[:b] + digit + text_line[b:]
        if a > -1:
            text_line = text_line[:a] + digit + text_line[a:]
    return text_line


def calculate_value(input_text):
    value = 0
    first_match = re.search(r'[0-9]', input_text)
    last_match = re.search(r'[0-9]', input_text[::-1])
    if first_match and last_match:
        value = int(f"{first_match.group()}{last_match.group()}")
    return value


def part_one(running_total=0):
    with open("input.txt", "r") as input_file:
        for text_line in input_file:
            running_total += calculate_value(text_line)
    print(f"part_one Result: {running_total}")


def test_part_one(running_total=0):
    test_input = """1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet"""

    for text_line in test_input.split('\n'):
        running_total += calculate_value(text_line)

    print(f"Test part_one Result: {running_total}")


def reverse_text_string(str):
    return str[::-1]


def part_two(running_total=0):
    with open("input.txt", "r") as input_file:
        for text_line in input_file:
            parsed_line = text_to_digits(text_line)
            value = calculate_value(parsed_line)
            running_total += value
    print(f"part_two Result: {running_total}")


def test_part_two(running_total=0):
    test_input = """two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen"""

    for text_line in test_input.split('\n'):
        parsed_line = text_to_digit(text_line)
        value = calculate_value(parsed_line)
        running_total += value

    print(f"Test Result: {running_total}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
