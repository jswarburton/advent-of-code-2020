from day_02 import (
    char_count_password_validator,
    char_position_password_validator,
    count_valid_passwords,
)


def test_char_count_password_validator():
    input = [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc",
    ]
    assert count_valid_passwords(input, char_count_password_validator) == 2


def test_char_position_password_validator():
    input = [
        "1-3 a: abcde",  # valid: position 1 contains a and position 3 does not
        "1-3 b: cdefg",  # invalid: neither position 1 nor position 3 contains b
        "2-9 c: ccccccccc",  # invalid: both position 2 and position 9 contain c
    ]
    assert count_valid_passwords(input, char_position_password_validator) == 1
