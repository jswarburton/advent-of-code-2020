from main.day_12 import solve_1, solve_2

input = [
    "F10",
    "N3",
    "F7",
    "R90",
    "F11",
]


def test_solve_1():
    assert solve_1(input) == 25


def test_solve_2():
    assert solve_2(input) == 286
