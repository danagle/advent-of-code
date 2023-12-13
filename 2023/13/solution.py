
def read_input_file():
    return [block.splitlines() for block in open("input.txt").read().split("\n\n")]


def find_reflection(pattern, smudges=0):
    for i in range(len(pattern)):
        if i+1 == len(pattern):
            return 0
        pairs = [(a, b) for line_a, line_b in zip(pattern[i::-1], pattern[i+1:])
                 for a, b in zip(line_a, line_b)]
        if len(pairs) - smudges == sum(1 for a, b in pairs if a == b):
            return i + 1


def part_one(patterns):
    return sum([(100 * find_reflection(pattern) + find_reflection(list(zip(*pattern))))
               for pattern in patterns])


def part_two(patterns):
    return sum([(100 * find_reflection(pattern, 1) + find_reflection(list(zip(*pattern)), 1))
               for pattern in patterns])


if __name__ == "__main__":
    from time import time
    from statistics import median

    pattern_data = read_input_file()
    et = []
    for _ in range(1):
        st = time()
        p1 = part_one(pattern_data)
        p2 = part_two(pattern_data)
        et.append(time() - st)
    print(f"Execution time: {median(et)}")
    print(f"part_one: {p1}")
    print(f"part_two: {p2}")
