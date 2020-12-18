from main.day_18 import solve, solve_1, solve_2, solve_advanced

input = [
    "2 * 3 + (4 * 5)",
    "5 + (8 * 3 + 9 + 3 * 4 * 3)",
    "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
    "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2",
]


def test_solve():
    assert solve("2 * 3 + 4 * 5") == 50
    assert solve("2 * 3 + (4 * 5)") == 26
    assert solve("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
    assert solve("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
    assert solve("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6)") == 6810
    assert solve("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632
    assert solve("(1 * 2) + (3 * 4)") == 14


def test_solve_advanced():
    assert solve_advanced("1 + (2 * 3) + (4 * (5 + 6))") == 51
    assert solve_advanced("2 * 3 + (4 * 5)") == 46
    assert solve_advanced("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 1445
    assert solve_advanced("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 669060
    assert solve_advanced("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 23340


def test_solve_1():
    assert solve_1(input) == 26335


def test_solve_2():
    assert solve_2(input) == 693891
