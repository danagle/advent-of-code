from functools import lru_cache


def read_input_file():
    return [(s, tuple([int(n) for n in d.split(",")]))
            for s, d in [l.split(" ")
                         for l in [x.strip()
                                   for x in open("input.txt").readlines()]]]


def part_one(records):
    return sum([arrangements(a, b) for a, b in records])


def part_two(records):
    return sum([arrangements('?'.join([a, a, a, a, a]), b * 5) for a, b in records])


@lru_cache(maxsize=None)
def arrangements(springs, damaged):
    if len(springs) == 0:
        # Springs is empty, check if damaged is empty -> 1 otherwise 0
        return 1 if len(damaged) == 0 else 0
    if springs.startswith("."):
        # Remove leading and trailing "." and try again
        return arrangements(springs.strip("."), damaged)
    if springs.startswith("?"):
        # Two possibilities so replace leading "?" with "#" and "." and try both options
        return (arrangements(springs.replace("?", "#", 1), damaged) +
                arrangements(springs.replace("?", ".", 1), damaged))
    if springs.startswith("#"):
        # Is damaged empty -> 0
        if len(damaged) == 0:
            return 0
        # Are there fewer springs than in the damaged group -> 0
        if len(springs) < damaged[0]:
            return 0
        # Will a "." prevent the placement of the next damaged group -> 0
        if any(s == "." for s in springs[0:damaged[0]]):
            return 0
        # If there are multiple damaged groups remaining ...
        if len(damaged) > 1:
            # Are there more damaged than there are springs -> 0
            if len(springs) < damaged[0] + 1:
                return 0
            # There must be a "." after a group -> 0
            if springs[damaged[0]] == "#":
                return 0
            # Try the next damaged block
            return arrangements(springs[damaged[0] + 1:], damaged[1:])
        else:
            # Assign the damaged block and try the next one
            return arrangements(springs[damaged[0]:], damaged[1:])


if __name__ == "__main__":
    from time import time
    from statistics import median

    data = read_input_file()

    et = []
    for _ in range(100):
        st = time()
        p1 = part_one(data)
        p2 = part_two(data)
        et.append(time() - st)

    print(f"Median Execution Time: {median(et)} seconds.")
    print(f"part_one: {p1}")
    print(f"part_two: {p2}")
