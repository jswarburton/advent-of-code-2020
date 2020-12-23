from main.day_23 import solve_1, solve_2


def test_solve_1():
    assert solve_1(list("389125467"), moves=10) == "92658374"
    assert solve_1(list("389125467"), moves=100) == "67384529"


def test_solve_2():
    assert solve_2(list("389125467"), num_cups=1_000_000, moves=10_000_000) == 149245887792
