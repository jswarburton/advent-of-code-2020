from main.file_reader import read


def solve_1(key_1: int, key_2: int) -> int:
    card_loop_size = calculate_loop_size(7, key_1)
    return pow(key_2, card_loop_size, 20201227)


def calculate_loop_size(subject_number, key):
    i = 1
    while pow(subject_number, i, 20201227) != key:
        i += 1

    return i


if __name__ == "__main__":
    input = read("day25-01.txt")
    print(solve_1(int(input[0]), int(input[1])))  # 19924389
