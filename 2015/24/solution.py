"""
Advent of Code 2015
Day 24: It Hangs in the Balance
https://adventofcode.com/2015/day/24
"""
from math import prod as math_prod
from z3 import Optimize, Int, If, sat


def read_input_file():
    return list(map(int, open("input.txt", "r").read().splitlines()))


def first_group_quantum_entanglement(packages, groups):
    weight_limit = sum(packages) // groups
    optimize = Optimize()
    variables = [(Int(str(x)), x) for x in packages]

    for v, _ in variables:
        optimize.add(v >= 0)
        optimize.add(v < groups)

    for i in range(groups - 1):
        optimize.add(sum(If(v == i, n, 0) for v, n in variables) == weight_limit)

    count = sum(If(v == 0, 1, 0) for v, _ in variables)
    quantum_entanglement = math_prod(If(v == 0, n, 1) for v, n in variables)

    optimize.minimize(count)
    optimize.minimize(quantum_entanglement)

    assert optimize.check() == sat
    return optimize.model().eval(quantum_entanglement).as_long()


if __name__ == "__main__":
    package_weights = read_input_file()
    print("Part 1:", first_group_quantum_entanglement(package_weights, 3))
    print("Part 2:", first_group_quantum_entanglement(package_weights, 4))
