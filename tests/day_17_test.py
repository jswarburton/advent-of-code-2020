from main.day_17 import solve_1, solve_2

input = [
    ".#.",
    "..#",
    "###",
]


def test_solve_1():
    assert solve_1(input) == 112


def test_solve_2():
    assert solve_2(input) == 848
