"""
Advent of Code 2017
Day 24: Electromagnetic Moat
https://adventofcode.com/2017/day/24
"""


def read_input_file():
    return sorted([tuple(sorted(map(int, component.split("/"))))
                   for component in open("input.txt", "r").read().splitlines()])


def build_bridges(components):
    built_bridges = []

    def extend_bridge(bridge, available, connection):
        nonlocal built_bridges
        component_found = False
        for component in available:
            if connection in component:
                component_found = True
                next_connection = component[0]
                if connection == component[0]:
                    next_connection = component[1]
                bridge.append(component)
                available.remove(component)
                extend_bridge(bridge, available, next_connection)
                component = bridge.pop()
                available.add(component)
        if not component_found:
            bridge_strength = sum(list(map(sum, list(bridge))))
            built_bridges.append((bridge_strength, len(bridge)))

    extend_bridge([], set(components), 0)
    part_one = sorted(built_bridges, reverse=True)[0][0]
    part_two = sorted(built_bridges, key=lambda t: t[1], reverse=True)[0][0]
    print(f"{part_one=}, {part_two=}")


if __name__ == "__main__":
    bridge_components = read_input_file()
    build_bridges(bridge_components)
