"""
Advent of Code 2019
Day 5: Sunny with a Chance of Asteroids
https://adventofcode.com/2019/day/5
"""


def read_input_file():
    return list(map(int, open("input.txt", "r").read().strip().split(",")))


def intcode_run(ops, input_id):
    ip = diagnostic_code = 0
    while ops[ip] != 99:
        args = {1: ops[ip + 1] if int((ops[ip] % 1000) / 100) else ops[ops[ip + 1]],
                2: ops[ip + 2] if int((ops[ip] % 10000) / 1000) or ops[ip] % 100 == 4 else ops[ops[ip + 2]]}
        instruction = ops[ip] % 100
        instruction_func = {
            1: (ops[ip + 3], args[1] + args[2], ip + 4),
            2: (ops[ip + 3], args[1] * args[2], ip + 4),
            3: (ops[ip + 1], input_id, ip + 2),
            4: (0, ops[0], ip + 2),
            5: (0, ops[0], args[2] if args[1] else ip + 3),
            6: (0, ops[0], args[2] if not args[1] else ip + 3),
            7: (ops[ip + 3], int(args[1] < args[2]), ip + 4),
            8: (ops[ip + 3], int(args[1] == args[2]), ip + 4)
        }[instruction]
        ops[instruction_func[0]] = instruction_func[1]
        ip = instruction_func[2]
        if instruction == 4:
            diagnostic_code = args[1]
    return diagnostic_code


def part_one():
    operations_list = read_input_file()
    print(intcode_run(operations_list, 1))


def part_two():
    operations_list = read_input_file()
    print(intcode_run(operations_list, 5))


if __name__ == "__main__":
    part_one()
    part_two()
