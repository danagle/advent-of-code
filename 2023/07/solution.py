from collections import Counter
from functools import cmp_to_key
from itertools import chain


def read_input_file():
    return [
        (hands, int(bids))
        for hands, bids
        in map(str.split, open("input.txt", "r"))
    ]


def get_hand_type(cards_hand):
    card_counts = Counter(cards_hand)
    kind_counts = tuple(
        count
        for _, count
        in card_counts.most_common()
    )
    hand_types = (
        (1, 1, 1, 1, 1),
        (2, 1, 1, 1),
        (2, 2, 1),
        (3, 1, 1),
        (3, 2),
        (4, 1),
        (5,)
    )
    return str(hand_types.index(kind_counts) + 1)


def get_compare_hands_func(card_values="23456789TJQKA"):

    def card_strength(card):
        return card_values.index(card)

    def compare_two_hands(hand_1, hand_2):
        compare_result = 0
        hand1_strength = [
            card_strength(c)
            for c
            in hand_1[0]
        ]
        hand2_strength = [
            card_strength(c)
            for c
            in hand_2[0]
        ]
        for i in range(len(hand_1[0])):
            if hand1_strength < hand2_strength:
                compare_result = -1
                break
        return compare_result

    return compare_two_hands


def get_best_joker_hand(cards_hand):
    cards = Counter(cards_hand.replace("J", ""))
    replacement_card = tuple(
        card
        for card, _
        in cards.most_common()
    )[0]
    return cards_hand.replace("J", replacement_card)


def process_hands_bids(hands_bids_list, extra_steps=False):
    card_values = "X23456789TJQKA"
    if extra_steps:
        part_number = "two"
        card_values = "X23456789TJQKA".replace("X", "J")
    else:
        part_number = "one"

    hands_by_type = dict()
    for hand_type_number in [str(n) for n in range(1, 8)]:
        hands_by_type[hand_type_number] = list()

    for hand_bid in hands_bids_list:
        hand_cards = hand_bid[0]
        if extra_steps:
            jokers = hand_cards.count("J")
            if 0 < jokers < 5:
                hand_cards = get_best_joker_hand(hand_cards)
        hands_by_type[get_hand_type(hand_cards)].append(hand_bid)

    compare_hands_func = get_compare_hands_func(card_values)

    result = sum([
        i * bid
        for i, (_, bid) in
        enumerate(list(chain(*[
            sorted(hands_by_type[key],
                   key=cmp_to_key(compare_hands_func))
            for key in
            sorted(hands_by_type.keys())])),
                  start=1)
    ])

    print(f"part_{part_number}: {result}")


if __name__ == "__main__":
    data = read_input_file()
    process_hands_bids(data)  # 249204891
    process_hands_bids(data, True)   # 249666369
