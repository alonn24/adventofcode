import numpy as np

"""
--- Day 7: Camel Cards ---
Sort the hands of cards and calculate the score based on the rand and the bid
"""


def part1(_input):
    def get_sorted_hands(data):
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
            return 7 if is_five_of_a_kind else \
                6 if is_four_of_a_kind else \
                5 if is_full_house else \
                4 if is_three_of_a_kind else \
                3 if is_two_pairs else \
                2 if is_one_pair else \
                1

        hand_types = np.vectorize(get_hand_type)(data[:, 0])
        sorted_hands = np.array([]).reshape(-1, 2)
        # Internally sort each hand type and stack back
        for hand_type in range(1, 8):
            hands_of_type = data[hand_types == hand_type]
            sorted_hands_of_type = sorted(hands_of_type, key=lambda x: (order.index(x[0][0]), order.index(
                x[0][1]), order.index(x[0][2]), order.index(x[0][3]), order.index(x[0][4])))
            if len(sorted_hands_of_type):
                sorted_hands = np.vstack([sorted_hands, sorted_hands_of_type])
        return sorted_hands

    data = np.array([x.split(' ') for x in _input])
    sorted_data = get_sorted_hands(data)
    factors = np.arange(1, len(sorted_data) + 1)
    return np.sum(sorted_data[:, 1].astype(int) * factors)


"""
--- Day 7: Camel Cards ---
Now use J and a Jocker that can act as any card
"""


def part2(_input):
    def get_sorted_hands(data):
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
            score = 7 if is_five_of_a_kind else \
                7 if is_four_of_a_kind and j_count == 1 else \
                6 if is_four_of_a_kind else \
                5 if is_full_house else \
                7 if is_three_of_a_kind and j_count == 2 else \
                6 if is_three_of_a_kind and j_count == 1 else \
                4 if is_three_of_a_kind else \
                5 if is_two_pairs and j_count == 1 else \
                3 if is_two_pairs else \
                7 if is_one_pair and j_count == 3 else \
                6 if is_one_pair and j_count == 2 else \
                4 if is_one_pair and j_count == 1 else \
                2 if is_one_pair else \
                7 if j_count == 5 else \
                7 if j_count == 4 else \
                6 if j_count == 3 else \
                4 if j_count == 2 else \
                2 if j_count == 1 else \
                1
            return score

        hand_types = np.vectorize(get_hand_type)(data[:, 0])

        # Internally sort each hand type and stack back
        sorted_hands = np.array([]).reshape(-1, 2)
        for hand_type in range(1, 8):
            hands_of_type = data[hand_types == hand_type]
            sorted_hands_of_type = sorted(hands_of_type, key=lambda x: (order.index(x[0][0]), order.index(
                x[0][1]), order.index(x[0][2]), order.index(x[0][3]), order.index(x[0][4])))
            # Failed to add an empty array because of missing shape, so we check
            if len(sorted_hands_of_type):
                sorted_hands = np.vstack([sorted_hands, sorted_hands_of_type])
        return sorted_hands

    data = np.array([x.split(' ') for x in _input])
    sorted_data = get_sorted_hands(data)
    factors = np.arange(1, len(sorted_data) + 1)
    return np.sum(sorted_data[:, 1].astype(int) * factors)
