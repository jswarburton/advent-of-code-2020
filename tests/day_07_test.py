from main.day_07 import parse, solve_1, solve_2


def test_parse():
    line = "light red bags contain 1 bright white bag, 2 muted yellow bags."
    assert parse(line) == ("light red", {"bright white": 1, "muted yellow": 2})


def test_parse_no_other_bags():
    line = "faded blue bags contain no other bags."
    assert parse(line) == ("faded blue", {})


def test_solve_1():
    input = [
        "light red bags contain 1 bright white bag, 2 muted yellow bags.",
        "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
        "bright white bags contain 1 shiny gold bag.",
        "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
        "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
        "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
        "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
        "faded blue bags contain no other bags.",
        "dotted black bags contain no other bags.",
    ]
    assert solve_1(input) == 4


def test_solve_2():
    input = [
        "shiny gold bags contain 2 dark red bags.",
        "dark red bags contain 2 dark orange bags.",
        "dark orange bags contain 2 dark yellow bags.",
        "dark yellow bags contain 2 dark green bags.",
        "dark green bags contain 2 dark blue bags.",
        "dark blue bags contain 2 dark violet bags.",
        "dark violet bags contain no other bags.",
    ]
    assert solve_2(input) == 126
