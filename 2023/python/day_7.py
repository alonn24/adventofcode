import numpy as np


def get_sorted_hands(data):
    order = "23456789TJQKA"

    def get_hand_type(hand):
        cards_count = np.bincount([order.index(card)
                                  for card in hand], minlength=len(order))
        sorted_counts = np.sort(cards_count)[::-1]
        if sorted_counts[0] == 5:
            return 7
        elif sorted_counts[0] == 4:
            return 6
        elif sorted_counts[0] == 3 and sorted_counts[1] == 2:
            return 5
        elif sorted_counts[0] == 3:
            return 4
        elif sorted_counts[0] == 2 and sorted_counts[1] == 2:
            return 3
        elif sorted_counts[0] == 2:
            return 2
        else:
            return 1

    hand_types = np.array([get_hand_type(hand) for hand in data[:, 0]])
    sorted_hands = np.array([]).reshape(-1, 2)
    for hand_type in range(1, 8):
        hands_of_type = data[hand_types == hand_type]
        print(hand_type, hands_of_type)
        sorted_hands_of_type = sorted(hands_of_type, key=lambda x: (order.index(x[0][0]), order.index(
            x[0][1]), order.index(x[0][2]), order.index(x[0][3]), order.index(x[0][4])))
        if len(sorted_hands_of_type):
            sorted_hands = np.vstack([sorted_hands, sorted_hands_of_type])
    return sorted_hands


def part1(_input):
    print('')
    data = np.array([x.split(' ') for x in _input])
    sorted_data = get_sorted_hands(data)
    factors = np.arange(1, len(sorted_data) + 1)
    return np.sum(sorted_data[:, 1].astype(int) * factors)
