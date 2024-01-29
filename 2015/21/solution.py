"""
Advent of Code 2015
Day 21: RPG Simulator 20XX
https://adventofcode.com/2015/day/21
"""
from itertools import product
from sys import maxsize


def read_input_file():
    return tuple(map(int, map(lambda x: x.split(': ')[1], open("input.txt", "r").read().splitlines())))


def both_parts(boss_stats):
    base_boss_hp, boss_damage, boss_armor = boss_stats

    weapons = [
        (8, 4, 0),
        (10, 5, 0),
        (25, 6, 0),
        (40, 7, 0),
        (74, 8, 0)
    ]

    armors = [
        (0, 0, 0),  # no armor
        (13, 0, 1),
        (31, 0, 2),
        (53, 0, 3),
        (75, 0, 4),
        (102, 0, 5)
    ]

    rings = [
        (0, 0, 0),  # no ring 1
        (0, 0, 0),  # no ring 2
        (25, 1, 0),
        (50, 2, 0),
        (100, 3, 0),
        (20, 0, 1),
        (40, 0, 2),
        (80, 0, 3)
    ]

    def player_wins(player_damage, player_armor):
        nonlocal base_boss_hp, boss_damage, boss_armor
        player_hp = 100
        boss_hp = base_boss_hp

        while True:
            boss_hp -= player_damage - boss_armor
            if boss_hp <= 0:
                return True

            player_hp -= boss_damage - player_armor
            if player_hp <= 0:
                return False

    min_cost = maxsize
    max_cost = maxsize * -1
    for weapon, armor, ring_1 in product(weapons, armors, rings):
        for ring_2 in rings:
            if ring_2 is ring_1:
                continue

            cost = weapon[0] + armor[0] + ring_1[0] + ring_2[0]
            if cost >= min_cost:
                continue

            if player_wins(weapon[1] + ring_1[1] + ring_2[1], armor[2] + ring_1[2] + ring_2[2]):
                if cost < min_cost:
                    min_cost = cost
            else:
                if cost > max_cost:
                    max_cost = cost

    return min_cost, max_cost


if __name__ == "__main__":
    boss_data = read_input_file()
    part_one, part_two = both_parts(boss_data)
    print(f"{part_one=}, {part_two=}")
