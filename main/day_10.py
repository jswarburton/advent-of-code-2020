from collections import defaultdict

from main.file_reader import read


def solve_1(input: list) -> int:
    input.sort()

    num_diffs_1 = 0
    num_diffs_3 = 1

    previous = 0
    for i in input:
        if i - previous == 1:
            num_diffs_1 += 1
        elif i - previous == 3:
            num_diffs_3 += 1

        previous = i

    return num_diffs_1 * num_diffs_3


def solve_2(input: list) -> int:
    input.sort()

    num_paths_to_val = defaultdict(int)
    num_paths_to_val[0] = 1

    for i in input:
        num_paths_to_val[i] = (
            num_paths_to_val[i - 1] + num_paths_to_val[i - 2] + num_paths_to_val[i - 3]
        )

    return num_paths_to_val[input.pop()]


if __name__ == "__main__":
    input = [int(n) for n in read("day10-01.txt")]
    print(solve_1(input))  # 1690
    print(solve_2(input))  # 5289227976704
