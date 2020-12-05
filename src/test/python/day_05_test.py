from day_05 import _calculate_row_id, find_highest_row_id


def test_calculate_row_id():
    assert _calculate_row_id("FBFBBFFRLR") == 357
    assert _calculate_row_id("FFFBBBFRRR") == 119
    assert _calculate_row_id("BBFFBBFRLL") == 820


def test_find_highest_row_id():
    codes = [
        "FBFBBFFRLR",
        "FFFBBBFRRR",
        "BBFFBBFRLL",
    ]

    assert find_highest_row_id(codes) == 820
