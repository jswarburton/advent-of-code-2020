from file_reader import read


def find_sum_in_preamble(target: int, preamble: list) -> bool:
    counts = dict()
    for i in preamble:
        counts[i] = counts.get(i, 0) + 1

    for i in preamble:
        complement = target - i
        if complement in counts and (complement != i or counts[i] > 1):
            return i * complement


def solve_1(input: list, preamble_length=25) -> int:
    for i in range(preamble_length, len(input)):
        start = i - preamble_length
        preamble = input[start:i]
        target = input[i]

        if not find_sum_in_preamble(target=target, preamble=preamble):
            return target


def solve_2(input: list, target: int) -> int:
    for start in range(len(input)):
        for end in range(start + 1, len(input)):
            slice = input[start:end]
            if sum(slice) == target:
                return min(slice) + max(slice)


if __name__ == "__main__":
    input = [int(n) for n in read("day09-01.txt")]
    print(solve_1(input))  # 88311122
    print(solve_2(input, 88311122))  # 13549369
