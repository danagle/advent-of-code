from itertools import cycle
from math import lcm
from re import findall


def read_input_file():
    with open("input.txt", "r") as input_file:
        lines = input_file.read().splitlines()
        instructions = [
            0 if instruction == "L"
            else 1
            for instruction
            in lines[0]
        ]
        nodes = {
            label: (left, right)
            for line
            in lines[2:]
            for label, left, right
            in [tuple(findall(r"\w+", line))]
        }
        return instructions, nodes


def part_one(instructions, nodes):
    label = "AAA"
    for step, instruction in enumerate(cycle(instructions)):
        if label == "ZZZ":
            break
        label = nodes[label][instruction]
    return step


def part_two_exploration(instructions, nodes):
    starting_labels = [
        label
        for label
        in nodes.keys()
        if label.endswith("A")
    ]
    print(f"starting_labels: {len(starting_labels)} {starting_labels}")
    ending_labels = [
        label
        for label
        in nodes.keys()
        if label.endswith("Z")
    ]
    print(f"ending_labels: {len(ending_labels)} {ending_labels}")

    all_cycles = []

    for label in starting_labels:
        found_z = None
        current_cycle = []
        current_cycle_steps = 0
        current_cycle_instructions = instructions

        while True:
            while current_cycle_steps == 0 or not label.endswith("Z"):
                current_cycle_steps += 1
                label = nodes[label][current_cycle_instructions[0]]
                current_cycle_instructions = current_cycle_instructions[1:] + [current_cycle_instructions[0]]

            current_cycle.append(current_cycle_steps)

            if found_z is None:
                found_z = label
                all_cycles.append(current_cycle_steps)
                current_cycle_steps = 0
            elif found_z == label:
                all_cycles.append(current_cycle_steps)
                break
            elif found_z in ending_labels:
                all_cycles.append(current_cycle_steps)
                current_cycle_steps = 0

    print([steps for steps in all_cycles])
    # [16343, 16343, 11911, 11911, 20221, 20221, 21883, 21883, 13019, 13019, 19667, 19667]
    # Observations :
    # (__A -> __Z) is the same number of steps as (__Z -> __Z)
    # There is a single __Z label in each path
    # We can optimise by breaking the loop when the __Z label is encountered


def part_two(instructions, nodes):
    starting_labels = [
        label
        for label
        in nodes.keys()
        if label.endswith("A")
    ]
    steps_list = []
    for label in starting_labels:
        for step, instruction in enumerate(cycle(instructions)):
            if label.endswith("Z"):
                steps_list.append(step)
                break
            label = nodes[label][instruction]
    return lcm(*steps_list)


if __name__ == "__main__":

    import time

    overall_st = time.time()
    i, n = read_input_file()
    part_two_exploration(i, n)
    st_1 = time.time()
    print(part_one(i, n))  # 13,019
    et_1 = time.time()
    st_2 = time.time()
    print(part_two(i, n))  # 13,524,038,372,771
    et_2 = time.time()
    overall_et = time.time()
    print('read_input_data Execution time:', overall_st - st_1, 'seconds')
    print('part_one Execution time:', et_1 - st_1, 'seconds')
    print('part_two Execution time:', et_2 - st_2, 'seconds')
    print('Overall Execution time:', overall_et - overall_st, 'seconds')
