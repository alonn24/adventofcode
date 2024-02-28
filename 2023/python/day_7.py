import numpy as np

HAND_TYPES = {
    'FIVE_OF_A_KIND': 7,
    'FOUR_OF_A_KIND': 6,
    'FULL_HOUSE': 5,
    'THREE_OF_A_KIND': 4,
    'TWO_PAIRS': 3,
    'ONE_PAIR': 2,
    'HIGH_CARD': 1,
}


def get_sorted_hands(data, order, get_hand_type):
    hand_types = np.vectorize(get_hand_type)(data[:, 0])
    sorted_hands = np.array([]).reshape(-1, 2)
    # Internally sort each hand type and stack back
    for hand_type in range(1, len(HAND_TYPES) + 1):
        hands_of_type = data[hand_types == hand_type]
        sorted_hands_of_type = sorted(hands_of_type, key=lambda x: (order.index(x[0][0]), order.index(
            x[0][1]), order.index(x[0][2]), order.index(x[0][3]), order.index(x[0][4])))
        if len(sorted_hands_of_type):
            sorted_hands = np.vstack([sorted_hands, sorted_hands_of_type])
    return sorted_hands


def part1(_input):
    """
      --- Day 7 Part 1: Camel Cards ---
      Sort the hands of cards and calculate the score based on the rand and the bid
    """
    order = "23456789TJQKA"

    def get_hand_type(hand):
        cards_count = np.bincount([order.index(card)
                                  for card in hand], minlength=len(order))
        sorted_counts = np.sort(cards_count)[::-1]
        is_five_of_a_kind = sorted_counts[0] == 5
        is_four_of_a_kind = sorted_counts[0] == 4
        is_full_house = sorted_counts[0] == 3 and sorted_counts[1] == 2
        is_three_of_a_kind = sorted_counts[0] == 3
        is_two_pairs = sorted_counts[0] == 2 and sorted_counts[1] == 2
        is_one_pair = sorted_counts[0] == 2
        return HAND_TYPES['FIVE_OF_A_KIND'] if is_five_of_a_kind else \
            HAND_TYPES['FOUR_OF_A_KIND'] if is_four_of_a_kind else \
            HAND_TYPES['FULL_HOUSE'] if is_full_house else \
            HAND_TYPES['THREE_OF_A_KIND'] if is_three_of_a_kind else \
            HAND_TYPES['TWO_PAIRS'] if is_two_pairs else \
            HAND_TYPES['ONE_PAIR'] if is_one_pair else \
            HAND_TYPES['HIGH_CARD']
    hands_data = np.array([x.split(' ') for x in _input])
    sorted_data = get_sorted_hands(hands_data, order, get_hand_type)
    factors = np.arange(1, len(sorted_data) + 1)
    return np.sum(sorted_data[:, 1].astype(int) * factors)


def part2(_input):
    """
      --- Day 7 Part 1: Camel Cards ---
      Now use J and a Jocker that can act as any card
    """

    order = "J23456789TQKA"

    def get_hand_type(hand):
        cards_count = np.bincount([order.index(card)
                                  for card in hand], minlength=len(order))
        sorted_counts = np.sort(cards_count[1:])[::-1]
        j_count = cards_count[0]
        is_five_of_a_kind = sorted_counts[0] == 5
        is_four_of_a_kind = sorted_counts[0] == 4
        is_full_house = sorted_counts[0] == 3 and sorted_counts[1] == 2
        is_three_of_a_kind = sorted_counts[0] == 3
        is_two_pairs = sorted_counts[0] == 2 and sorted_counts[1] == 2
        is_one_pair = sorted_counts[0] == 2
        score = HAND_TYPES['FIVE_OF_A_KIND'] if is_five_of_a_kind else \
            HAND_TYPES['FIVE_OF_A_KIND'] if is_four_of_a_kind and j_count == 1 else \
            HAND_TYPES['FOUR_OF_A_KIND'] if is_four_of_a_kind else \
            HAND_TYPES['FULL_HOUSE'] if is_full_house else \
            HAND_TYPES['FIVE_OF_A_KIND'] if is_three_of_a_kind and j_count == 2 else \
            HAND_TYPES['FOUR_OF_A_KIND'] if is_three_of_a_kind and j_count == 1 else \
            HAND_TYPES['THREE_OF_A_KIND'] if is_three_of_a_kind else \
            HAND_TYPES['FULL_HOUSE'] if is_two_pairs and j_count == 1 else \
            HAND_TYPES['TWO_PAIRS'] if is_two_pairs else \
            HAND_TYPES['FIVE_OF_A_KIND'] if is_one_pair and j_count == 3 else \
            HAND_TYPES['FOUR_OF_A_KIND'] if is_one_pair and j_count == 2 else \
            HAND_TYPES['THREE_OF_A_KIND'] if is_one_pair and j_count == 1 else \
            HAND_TYPES['ONE_PAIR'] if is_one_pair else \
            HAND_TYPES['FIVE_OF_A_KIND'] if j_count == 5 else \
            HAND_TYPES['FIVE_OF_A_KIND'] if j_count == 4 else \
            HAND_TYPES['FOUR_OF_A_KIND'] if j_count == 3 else \
            HAND_TYPES['THREE_OF_A_KIND'] if j_count == 2 else \
            HAND_TYPES['ONE_PAIR'] if j_count == 1 else \
            HAND_TYPES['HIGH_CARD']
        return score

    hands_data = np.array([x.split(' ') for x in _input])
    sorted_data = get_sorted_hands(hands_data, order, get_hand_type)
    factors = np.arange(1, len(sorted_data) + 1)
    return np.sum(sorted_data[:, 1].astype(int) * factors)
