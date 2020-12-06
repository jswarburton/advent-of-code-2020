from day_06 import count_anyone_in_group_answer_yes, count_everyone_in_group_answer_yes

input = [
    "abc",
    "",
    "a",
    "b",
    "c",
    "",
    "ab",
    "ac",
    "",
    "a",
    "a",
    "a",
    "a",
    "",
    "b",
]


def test_count_anyone_in_group_answer_yes():
    assert count_anyone_in_group_answer_yes(input) == 11


def test_count_everyone_in_group_answer_yes():
    assert count_everyone_in_group_answer_yes(input) == 6
