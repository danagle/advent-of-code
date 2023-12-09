from itertools import pairwise


def read_input_file():
    return [list(map(int, line.split()))
            for line in open("input.txt", "r")]


def predict_value(history):
    return history[-1] + predict_value([right - left
                                        for left, right in pairwise(history)]) if any(history) else 0


def part_one(histories):
    return sum(map(predict_value, histories))


def part_two(histories):
    return sum(predict_value(list(reversed(history)))
               for history in histories)


if __name__ == "__main__":
    history_data = read_input_file()
    extrapolated_sum_1 = part_one(history_data)
    extrapolated_sum_2 = part_two(history_data)
    print(f"part_one : {extrapolated_sum_1}")
    print(f"part_two : {extrapolated_sum_2}")
