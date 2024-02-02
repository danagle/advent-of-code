"""
Advent of Code 2017
Day 18: Duet
https://adventofcode.com/2017/day/18
"""
from collections import defaultdict, deque


def read_input_file():
    return open("input.txt", "r").read().splitlines()


def part_one(instructions):
    registers, frequency, pointer = defaultdict(int), None, 0

    def get(value):
        nonlocal registers
        try:
            return int(value)
        except ValueError:
            return registers[value]

    while 0 <= pointer < len(instructions):
        tokens = instructions[pointer].split()
        pointer += 1
        match tokens[0]:
            case "snd":
                frequency = get(tokens[1])
            case "set":
                registers[tokens[1]] = get(tokens[2])
            case "add":
                registers[tokens[1]] += get(tokens[2])
            case "mul":
                registers[tokens[1]] *= get(tokens[2])
            case "mod":
                registers[tokens[1]] %= get(tokens[2])
            case "rcv":
                if get(tokens[1]) != 0:
                    break
            case "jgz":
                if get(tokens[1]) > 0:
                    pointer += get(tokens[2]) - 1
    print(frequency)


def part_two(instructions):
    state_one = defaultdict(int) | {"id": 0, "sent": 0, "waiting": 0, "p": 0}
    state_two = defaultdict(int) | {"id": 1, "sent": 0, "waiting": 0, "p": 1}
    queue_one, queue_two = deque(),  deque()
    pointer_one = pointer_two = 0

    def get_value(value, registers):
        if value in registers:
            return registers[value]
        return int(value)

    def process_instruction(pointer, registers, in_queue, out_queue):
        nonlocal instructions
        command, *params = instructions[pointer].split()
        match command:
            case "set":
                registers[params[0]] = get_value(params[1], registers)
            case "add":
                registers[params[0]] += get_value(params[1], registers)
            case "mul":
                registers[params[0]] *= get_value(params[1], registers)
            case "mod":
                registers[params[0]] %= get_value(params[1], registers)
            case "snd":
                out_queue.append(get_value(params[0], registers))
                registers["sent"] += 1
            case "jgz":
                if get_value(params[0], registers) > 0:
                    return pointer + get_value(params[1], registers)
            case "rcv":
                if len(in_queue) > 0:
                    registers[params[0]] = in_queue.popleft()
                    registers["waiting"] = 0
                else:
                    registers["waiting"] = 1
                    return pointer
        return pointer + 1

    while not state_one["waiting"] or not state_two["waiting"]:
        pointer_one = process_instruction(pointer_one, state_one, queue_one, queue_two)
        pointer_two = process_instruction(pointer_two, state_two, queue_two, queue_one)

    print(state_two["sent"])


if __name__ == "__main__":
    code = read_input_file()
    part_one(code)
    part_two(code)
