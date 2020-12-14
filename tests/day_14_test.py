from main.day_14 import solve_1, solve_2


def test_solve_1():
    input = [
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
        "mem[8] = 11",
        "mem[7] = 101",
        "mem[8] = 0",
    ]
    assert solve_1(input) == 165


def test_solve_2():
    input = [
        "mask = 000000000000000000000000000000X1001X",
        "mem[42] = 100",
        "mask = 00000000000000000000000000000000X0XX",
        "mem[26] = 1",
    ]
    assert solve_2(input) == 208
