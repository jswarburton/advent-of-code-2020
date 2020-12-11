from main.file_reader import read


def find_2020_product(nums: list) -> int:
    counts = dict()
    for n in nums:
        counts[n] = counts.get(n, 0) + 1

    for n in nums:
        complement = 2020 - n
        if complement in counts and (complement != n or counts[n] > 1):
            return n * complement


def find_2020_triple_product(nums: list) -> int:
    unique = set(nums)

    if len(unique) != len(nums):
        print("Solution might be a bit buggy here...")

    for n in nums:
        for m in nums:
            if n != m:
                complement = 2020 - (n + m)
                if complement in unique:
                    return n * m * complement


if __name__ == "__main__":
    nums = [int(n) for n in read("day01-01.txt")]
    print(find_2020_product(nums))
    print(find_2020_triple_product(nums))
