from functools import reduce

from main.file_reader import read


def solve_1(input: list) -> int:
    earliest_departure = int(input[0])
    busses = [int(bus) for bus in input[1].split(",") if bus != "x"]

    current_time = earliest_departure

    while True:
        for bus in busses:
            if current_time % bus == 0:
                return bus * (current_time - earliest_departure)

        current_time += 1


def solve_2(input: list) -> int:
    busses = [int(bus) for bus in input[1].split(",") if bus != "x"]
    remainders = [-index for (index, bus) in enumerate(input[1].split(",")) if bus != "x"]

    return chinese_remainder(busses, remainders)


# Copied from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
# Understanding from https://medium.com/free-code-camp/how-to-implement-the-chinese-remainder-theorem-in-java-db88a3f1ffe0
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


# As above
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


if __name__ == "__main__":
    input = read("day13-01.txt")
    print(solve_1(input))  # 4315
    print(solve_2(input))  # 556100168221141
