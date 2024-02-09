"""
Advent of Code 2018
Day 24: Immune System Simulator 20XX
https://adventofcode.com/2018/day/24
"""
from copy import deepcopy
from re import finditer


def read_input_file():
    armies, army, damage_type = [], {}, ""
    for line in open("input.txt", "r").read().splitlines():
        if not (line := line.strip()):
            continue
        if line.endswith(":"):
            army = {
                "id": len(armies),
                "name": line[:-1],
                "groups": []
            }
            armies.append(army)
        elif line[0].isdigit():
            group = {
                "id": "{a}:{b}".format(a=army["id"], b=len(army["groups"])),
                "team": army["id"],
                "weak": [],
                "immune": []
            }
            # Parse numeric values
            numeric_values = []
            for index, value in enumerate(finditer(r"\d+", line)):
                numeric_values.append(int(value.group()))
                if 2 == index:
                    group["attack"] = line[value.end()+1:].strip().split(" ")[0]
            group["units"] = numeric_values[0]
            group["health"] = numeric_values[1]
            group["damage"] = numeric_values[2]
            group["initiative"] = numeric_values[3]
            # Parse weaknesses or immunities
            if (left := line.find("(")) > -1:
                right = line.find(")")
                line_segment = line[left+1:right].replace(",", "")
                for segment in line_segment.split(";"):
                    tokens = segment.strip().split(" ")
                    group[tokens[0].strip()] = tokens[2:]
            army["groups"].append(group)
    return armies


def effective_power(group):
    # Each group also has an effective power:
    # the number of units in that group multiplied by their attack damage.
    return group["units"] * group["damage"]


def attack_selection_priority(group):
    # In decreasing order of effective power, groups choose their targets;
    # in a tie, the group with the higher initiative chooses first
    return effective_power(group), group["initiative"]


def target_priority(group, target):
    # If an attacking group is considering two defending groups to which it would deal equal damage,
    # it chooses to target the defending group with the largest effective power;
    # if there is still a tie, it chooses the defending group with the highest initiative.
    return attack_damage(group, target), effective_power(target), target["initiative"]


def target_selection_phase(groups):
    # In decreasing order of effective power, groups choose their targets;
    # in a tie, the group with the higher initiative chooses first
    groups.sort(key=lambda g: attack_selection_priority(g), reverse=True)
    selections, selected_targets = {}, set()
    for group in groups:
        targets = [g for g in groups if g["team"] != group["team"]]
        targets.sort(key=lambda t: target_priority(group, t), reverse=True)
        for target in targets:
            if attack_damage(group, target) > 0 and target["id"] not in selected_targets:
                selections[group["id"]] = target["id"]
                selected_targets.add(target["id"])
                break
    return selections


def attack_damage(group, target):
    #  By default, an attacking group would deal damage equal to its effective power to the defending group.
    #  if the defending group is immune to the attacking group's attack type, the defending group instead takes no damage;
    #  if the defending group is weak to the attacking group's attack type, the defending group instead takes double damage.
    attack_type = group["attack"]
    damage = effective_power(group)
    if attack_type in target["immune"]:
        damage = 0
    elif attack_type in target["weak"]:
        damage *= 2
    return damage


def fight(armies):
    fight_round = 0
    while all(sum(g["units"] for g in a["groups"]) for a in armies):
        # Avoid a deadlock
        if fight_round > 1_500:
            break
        fight_round += 1
        all_groups = list(filter(lambda g: g["units"] > 0, sum(map(lambda a: a["groups"], armies), [])))
        targets = target_selection_phase(all_groups)
        all_groups.sort(key=lambda g: g["initiative"], reverse=True)
        for group in all_groups:
            if group["id"] in targets:
                target = list(filter(lambda g: g["id"] == targets[group["id"]], all_groups))[0]
                target["units"] -= min(attack_damage(group, target) // target["health"], target["units"])

    return armies


def part_one(data):
    armies = fight(data)
    return sum(_["units"] for _ in sum(map(lambda a: a["groups"], armies), []))


def part_two(data):
    boost = 0
    while True:
        boosted = deepcopy(data)
        boost += 1

        for group in boosted[0]["groups"]:
            group["damage"] += boost

        boosted = fight(boosted)
        immune_units, infection_units = [sum([_["units"] for _ in boosted[s]["groups"]]) for s in range(len(boosted))]

        # The armies repeatedly fight until only Immune System has units remaining.
        if immune_units > infection_units == 0:
            break

    return immune_units


if __name__ == "__main__":
    armies_data = read_input_file()
    print(part_one(deepcopy(armies_data)))
    print(part_two(deepcopy(armies_data)))
