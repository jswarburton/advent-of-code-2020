from main.day_09 import solve_1, solve_2

input = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
]


def test_solve_1():
    assert solve_1(input, preamble_length=5) == 127


def test_solve_2():
    assert solve_2(input, 127) == 62
