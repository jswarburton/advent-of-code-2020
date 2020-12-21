from main.day_21 import solve_1, solve_2

input = [
    "mxmxvkd kfcds sqjhc nhms (contains dairy, fish)",
    "trh fvjkl sbzzf mxmxvkd (contains dairy)",
    "sqjhc fvjkl (contains soy)",
    "sqjhc mxmxvkd sbzzf (contains fish)",
]


def test_solve_1():
    assert solve_1(input) == 5


def test_solve_2():
    assert solve_2(input) == "mxmxvkd,sqjhc,fvjkl"
