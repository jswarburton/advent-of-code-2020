from main.file_reader import read


def count_valid_passwords(lines: list, is_valid) -> int:
    num_valid = 0
    for line in lines:
        first_part, password = line.split(": ")
        min_max, required_char = first_part.split(" ")
        min, max = min_max.split("-")

        if is_valid(password, required_char, int(min), int(max)):
            num_valid += 1

    return num_valid


def char_count_password_validator(password: str, required_char, min: int, max: int) -> bool:
    count_of_char = 0
    for char in password:
        if char == required_char:
            count_of_char += 1

    return min <= count_of_char <= max


def char_position_password_validator(password: str, required_char, pos1: int, pos2: int) -> bool:
    return (password[pos1 - 1] == required_char and not password[pos2 - 1] == required_char) or (
        not password[pos1 - 1] == required_char and password[pos2 - 1] == required_char
    )


if __name__ == "__main__":
    input = read("day02-01.txt")
    print(count_valid_passwords(input, char_count_password_validator))
    print(count_valid_passwords(input, char_position_password_validator))
