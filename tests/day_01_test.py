from main.day_01 import find_2020_product, find_2020_triple_product


def test_find_2020_product():
    assert find_2020_product([1721, 979, 366, 299, 675, 1456]) == 514579
    assert find_2020_product([1010, 1721, 299]) == 514579
    assert find_2020_product([1010, 1721, 1010]) == 1020100


def test_find_2020_triple_product():
    assert find_2020_triple_product([1721, 979, 366, 299, 675, 1456]) == 241861950
