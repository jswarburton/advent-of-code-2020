from day_11 import solve_1, solve_2

input = [
    "L.LL.LL.LL",
    "LLLLLLL.LL",
    "L.L.L..L..",
    "LLLL.LL.LL",
    "L.LL.LL.LL",
    "L.LLLLL.LL",
    "..L.L.....",
    "LLLLLLLLLL",
    "L.LLLLLL.L",
    "L.LLLLL.LL",
]


def test_solve_1():
    assert solve_1(input) == 37


def test_solve_2():
    assert solve_2(input) == 26
