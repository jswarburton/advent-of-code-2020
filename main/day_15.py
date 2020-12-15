from main.file_reader import read


def solve_1(input: list) -> int:
    return solve(input, num_to_speak=2020)


def solve_2(input: list) -> int:
    return solve(input, num_to_speak=30000000)


def solve(input: list, num_to_speak: int):
    spoken = {}
    spoken_num = -1
    next_spoken_num = -1
    for i in range(num_to_speak):
        spoken_num = input[i] if i < len(input) else next_spoken_num
        next_spoken_num = 0 if spoken_num not in spoken else i - spoken[spoken_num]
        spoken[spoken_num] = i
    return spoken_num


if __name__ == "__main__":
    input = [int(n) for n in read("day15-01.txt")[0].split(",")]
    print(solve_1(input))  # 1085
    print(solve_2(input))  # 10652
