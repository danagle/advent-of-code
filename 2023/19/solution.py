from math import prod
import re
from time import time


def read_input_file():
    text_blocks = [block for block in open("input.txt").read().strip().split("\n\n")]
    workflows_block, ratings_block = text_blocks
    ratings = [tuple(map(int, re.findall(r"\d+", line)))
               for line in ratings_block.splitlines()]
    workflow_rules = {line.split("{")[0]: line.split("{")[1][:-1].split(",")
                      for line in workflows_block.splitlines()}
    return workflow_rules, ratings


def total_category_ratings(workflow_rules, ratings):
    """
    Returns the sum of the category ratings of the part if it is accepted, 0 otherwise.
    """
    current = "in"
    comparison = {">": lambda a, b: a > b, "<": lambda a, b: a < b}
    while current not in ("A", "R"):
        instructions = workflow_rules[current]
        for rule in instructions:
            if ":" not in rule:
                current = rule
                break
            else:
                expression, outcome = rule.split(":")
                # expression : [0]: rating category, [1]: comparison operator, [2:]: value
                if comparison[expression[1]](ratings["xmas".index(expression[0])],
                                             int(expression[2:])):
                    current = outcome
                    break
    return sum(ratings) if current == "A" else 0


def part_one(rules, ratings):
    return sum([total_category_ratings(rules, part_ratings) for part_ratings in ratings])


def find_accepted_ranges(workflow_rules, rating_ranges):
    """
    Returns the list of category rating ranges that are accepted by the workflow rules.
    """
    accepted_list = []
    workflow_nodes = [("in", rating_ranges)]

    while len(workflow_nodes) > 0:
        workflow_label, rating_ranges = workflow_nodes.pop()
        for rule in workflow_rules[workflow_label]:
            if ":" in rule:
                category, condition, limit_str, result = re.findall(r"(\w)([><])(\d+):(\w+)", rule)[0]
                limit = int(limit_str)
                condition_ranges = rating_ranges.copy()
                if ">" == condition:
                    condition_ranges[category] = (limit + 1, condition_ranges[category][1])
                    rating_ranges[category] = (rating_ranges[category][0], limit)
                elif "<" == condition:
                    condition_ranges[category] = (condition_ranges[category][0], limit - 1)
                    rating_ranges[category] = (limit, rating_ranges[category][1])
                if result in ("A", "R"):
                    if result == "A":
                        accepted_list.append(condition_ranges.copy())
                else:
                    workflow_nodes.append((result, condition_ranges.copy()))
            else:
                if rule in ("A", "R"):
                    if rule == "A":
                        accepted_list.append(rating_ranges.copy())
                else:
                    workflow_nodes.append((rule, rating_ranges.copy()))

    return accepted_list


def part_two(workflow_rules):
    ranges = {category: range_list for category, range_list in zip(list("xmas"), [[1, 4000]] * 4)}
    accepted = find_accepted_ranges(workflow_rules, ranges)
    return sum([prod([(v[1] - v[0] + 1) for v in rng.values()]) for rng in accepted])


if __name__ == "__main__":
    workflows, category_ratings = read_input_file()
    st = time()
    p1 = part_one(workflows, category_ratings)
    p2 = part_two(workflows)
    print(f"Execution Time: {time() - st}")
    print(p1)
    print(p2)
