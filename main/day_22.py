import itertools
from collections import deque
from copy import deepcopy

from main.file_reader import read


def solve_1(input: list) -> int:
    p1_hand, p2_hand = parse(input)

    while p1_hand and p2_hand:
        p1_card, p2_card = p1_hand.pop(), p2_hand.pop()

        if p1_card > p2_card:
            p1_hand.appendleft(p1_card)
            p1_hand.appendleft(p2_card)
        else:
            p2_hand.appendleft(p2_card)
            p2_hand.appendleft(p1_card)

    winner = p2_hand if p2_hand else p1_hand

    return sum((i + 1) * val for i, val in enumerate(winner))


def solve_2(input: list) -> int:
    player1, player2 = parse(input)

    player1, player2 = play(deepcopy(player1), deepcopy(player2))

    winner = player2 if player2 else player1

    return sum((i + 1) * val for i, val in enumerate(winner))


def play(p1_hand, p2_hand):
    previously_seen_hands = set()

    while p1_hand and p2_hand:
        if (tuple(p1_hand), tuple(p2_hand)) in previously_seen_hands:
            return p1_hand, deque()
        previously_seen_hands.add((tuple(p1_hand), tuple(p2_hand)))

        p1_card, p2_card = p1_hand.pop(), p2_hand.pop()

        if len(p1_hand) >= p1_card and len(p2_hand) >= p2_card:
            sub_game_p1, sub_game_p2 = play(
                deque(itertools.islice(p1_hand, len(p1_hand) - p1_card, None)),
                deque(itertools.islice(p2_hand, len(p2_hand) - p2_card, None)),
            )

            if sub_game_p1:
                p1_hand.appendleft(p1_card)
                p1_hand.appendleft(p2_card)
            else:
                p2_hand.appendleft(p2_card)
                p2_hand.appendleft(p1_card)
        else:
            if p1_card > p2_card:
                p1_hand.appendleft(p1_card)
                p1_hand.appendleft(p2_card)
            else:
                p2_hand.appendleft(p2_card)
                p2_hand.appendleft(p1_card)

    return p1_hand, p2_hand


def parse(input: list) -> (deque, deque):
    player1 = deque()
    player2 = deque()

    parsing_p1 = False

    for line in input:
        if not line:
            continue
        elif "Player 1" in line:
            parsing_p1 = True
        elif "Player 2" in line:
            parsing_p1 = False
        elif parsing_p1:
            player1.appendleft(int(line))
        else:
            player2.appendleft(int(line))

    return player1, player2


if __name__ == "__main__":
    input = read("day22-01.txt")
    print(solve_1(input))  # 32824
    print(solve_2(input))  # 36515
