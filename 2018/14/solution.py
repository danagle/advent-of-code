"""
Advent of Code 2018
Day 14: Chocolate Charts
https://adventofcode.com/2018/day/14
"""


def read_input_file():
    return open("input.txt", "r").read().strip()


def part_one(puzzle_input):
    value = int(puzzle_input)
    recipe_scores = [3, 7]
    elf_1, elf_2 = 0, 1
    while len(recipe_scores) < value + 10:
        recipes_sum = recipe_scores[elf_1] + recipe_scores[elf_2]
        recipe_scores.extend(divmod(recipes_sum, 10) if recipes_sum >= 10 else (recipes_sum,))
        elf_1 = (elf_1 + 1 + recipe_scores[elf_1]) % len(recipe_scores)
        elf_2 = (elf_2 + 1 + recipe_scores[elf_2]) % len(recipe_scores)
    print("".join(str(score) for score in recipe_scores[value:value + 10]))


def part_two(puzzle_input):
    digits = [int(digit) for digit in puzzle_input]
    recipe_scores = [3, 7]
    elf_1, elf_2 = 0, 1
    while recipe_scores[-len(digits):] != digits and recipe_scores[-len(digits) - 1:-1] != digits:
        recipes_sum = recipe_scores[elf_1] + recipe_scores[elf_2]
        recipe_scores.extend(divmod(recipes_sum, 10) if recipes_sum >= 10 else (recipes_sum,))
        elf_1 = (elf_1 + 1 + recipe_scores[elf_1]) % len(recipe_scores)
        elf_2 = (elf_2 + 1 + recipe_scores[elf_2]) % len(recipe_scores)
    print(len(recipe_scores) - len(digits) - (0 if recipe_scores[-len(digits):] == digits else 1))


if __name__ == "__main__":
    previous_recipes = read_input_file()
    part_one(previous_recipes)
    part_two(previous_recipes)
