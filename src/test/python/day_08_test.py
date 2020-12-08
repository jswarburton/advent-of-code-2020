from day_08 import solve_1, solve_2

input = [
    "nop +0",
    "acc +1",
    "jmp +4",
    "acc +3",
    "jmp -3",
    "acc -99",
    "acc +1",
    "jmp -4",
    "acc +6",
]


def test_solve_1():
    assert solve_1(input) == 5


def test_solve_2():
    assert solve_2(input) == 8
