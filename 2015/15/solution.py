"""
Advent of Code 2015
Day 15: Science for Hungry People
https://adventofcode.com/2015/day/15
"""
from collections import defaultdict
from itertools import product


def read_input_file():
    ingredients = defaultdict(dict)
    lines = open("input.txt", "r").read().splitlines()
    for line in lines:
        ingredient, properties = line.split(": ")
        for property_value in properties.split(", "):
            name, value = property_value.split(" ")
            ingredients[ingredient][name.lower()] = int(value)
    return ingredients


def recipe_scores(ingredients):
    highest_score, calories_score, property_names = 0, 0, ("capacity", "durability", "flavor", "texture", "calories")
    for mixture in product(range(1, 101), range(1, 101), range(1, 101), range(1, 101)):
        if 100 != sum(mixture):
            continue
        frosting, candy, butterscotch, sugar = mixture
        cookie = {"Frosting": frosting, "Candy": candy, "Butterscotch": butterscotch, "Sugar": sugar,
                  "capacity": 0, "durability": 0, "flavor": 0, "texture": 0, "calories": 0}
        cookie_score = 1
        for property_name in property_names:
            for ingredient in ingredients:
                cookie[property_name] += ingredients[ingredient][property_name] * cookie[ingredient]
            if "calories" == property_name:
                continue
            cookie_score *= max(0, cookie[property_name])
        if 500 == cookie["calories"] and cookie_score > calories_score:
            calories_score = cookie_score
        if cookie_score > highest_score:
            highest_score = cookie_score
    return highest_score, calories_score


if __name__ == "__main__":
    ingredient_properties = read_input_file()
    part_one, part_two = recipe_scores(ingredient_properties)
    print(f"{part_one=}, {part_two=}")
