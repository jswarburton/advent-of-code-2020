from main.day_13 import solve_1, solve_2

input = [
    "939",
    "7,13,x,x,59,x,31,19",
]


def test_solve_1():
    assert solve_1(input) == 295


def test_solve_2():
    assert solve_2(input) == 1068781
