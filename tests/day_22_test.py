from main.day_22 import solve_1, solve_2

input = [
    "Player 1:",
    "9",
    "2",
    "6",
    "3",
    "1",
    "",
    "Player 2:",
    "5",
    "8",
    "4",
    "7",
    "10",
]


def test_solve_1():
    assert solve_1(input) == 306


def test_solve_2():
    assert solve_2(input) == 291


def test_solve_2_infinite_loop():
    input = [
        "Player 1:",
        "43",
        "19",
        "",
        "Player 2:",
        "2",
        "29",
        "14",
    ]
    assert solve_2(input) == 105
