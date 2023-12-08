from math import prod
from re import match


LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def get_possible_game_id(line):
    """
    Returns 0 if the game is impossible or else return the game ID.
    """
    colours_min = {k: 0 for k in list(LIMITS.keys())}
    game_info = match(r"Game (\d+): ", line)
    game_id = int(game_info.group(1))
    sets = game_info.string[game_info.end():]
    for set_ in sets.split("; "):
        for num_color in set_.split(", "):
            num, color = num_color.strip().split(" ")
            num = int(num.strip())
            if num !=0 and num > colours_min[color]:
                colours_min[color] = num
            if num > LIMITS[color.strip()]:
                return 0
    return game_id


def part_one():
    result = sum([get_possible_game_id(line)
                  for line in open("input.txt", "r").read().splitlines()])
    return result


def calculate_product_from_text(line):
    colours_min = {key: 0 for key in LIMITS.keys()}
    _, handfuls = line.split(": ")
    for handful in handfuls.split("; "):
        for num_colour in handful.split(", "):
            num, colour = num_colour.strip().split(" ")
            num = int(num)
            if num != 0 and num > colours_min[colour]:
                colours_min[colour] = num
    return prod(colours_min.values())


def part_two():
    result = sum([calculate_product_from_text(line)
                  for line in open("input.txt", "r").read().splitlines()])
    return result


if __name__ == "__main__":
    print(f"part_one: {part_one()}")
    print(f"part_two: {part_two()}")
