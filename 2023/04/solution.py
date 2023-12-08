import re


def read_input_file():
    content = []
    with open("input.txt", "r") as input_file:
        content = input_file.read().splitlines()
    return content


def set_from_numbers_string(numbers_string):
    return set([int(n) for n in re.findall(r'\d+', numbers_string)])


def list_card_matches():
    cards_stack = read_input_file()
    matches_list = []
    for line in cards_stack:
        winning_numbers, elfs_numbers = line.split(": ")[1].strip().split(" | ")
        winning_set = set_from_numbers_string(winning_numbers)
        elfs_set = set_from_numbers_string(elfs_numbers)
        matches_list.append(len(winning_set.intersection(elfs_set)))
    return matches_list


def part_one(card_matches_list):
    return sum([1 << (numbers - 1)
                for numbers in card_matches_list
                if numbers > 0])


def part_two(card_matches_list):
    scratch_cards = [0 for _ in range(len(card_matches_list))]
    for current_index, number_of_cards in enumerate(card_matches_list):
        if number_of_cards > 0:
            extra_cards = scratch_cards[current_index]
            for _ in range(extra_cards + 1):
                for next_card in range(1, number_of_cards + 1):
                    scratch_cards[current_index + next_card] += 1
    return sum(scratch_cards) + len(card_matches_list)  # 8063216


if __name__ == "__main__":
    import time
    overall_st = time.time()
    cards_list = list_card_matches()
    st_1 = time.time()
    points_total = part_one(cards_list)
    et_1 = time.time()
    st_2 = time.time()
    total_cards = part_two(cards_list)
    et_2 = time.time()
    overall_et = time.time()
    print('cards_list Execution time:', overall_st - st_1, 'seconds')
    print('part_one Execution time:', et_1 - st_1, 'seconds')
    print(f"Total points : {points_total}")
    print('part_two Execution time:', et_2 - st_2, 'seconds')
    print(f"Total number of cards : {total_cards}")
    print('Overall Execution time:', overall_et - overall_st, 'seconds')

