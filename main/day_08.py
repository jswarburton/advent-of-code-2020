from main.file_reader import read


def solve_1(input: list) -> int:
    index = 0
    accumulator = 0
    visited = set()

    while True:
        if index in visited:
            break
        visited.add(index)

        instruction, value = input[index].split(" ")

        if instruction == "acc":
            accumulator += int(value)
            index += 1
        elif instruction == "jmp":
            index += int(value)
        elif instruction == "nop":
            index += 1

    return accumulator


def solve_2(input: list) -> int:
    def rec(index: int, accumulator: int, visited: set, flipped: bool) -> int:
        if index in visited or index < 0 or index > len(input):
            return None
        elif index == len(input):
            return accumulator

        # make a copy so we don't mutate the set in the other recursions
        new_visited = visited.copy()
        new_visited.add(index)

        instruction, value = input[index].split(" ")

        if instruction == "acc":
            return rec(index + 1, accumulator + int(value), new_visited, flipped)

        elif instruction == "jmp":
            jmp_attempt = rec(index + int(value), accumulator, new_visited, flipped)
            nop_attempt = None if flipped else rec(index + 1, accumulator, new_visited, True)

            return nop_attempt if jmp_attempt is None else jmp_attempt

        elif instruction == "nop":
            nop_attempt = rec(index + 1, accumulator, new_visited, flipped)
            jmp_attempt = (
                None if flipped else rec(index + int(value), accumulator, new_visited, True)
            )

            return nop_attempt if jmp_attempt is None else jmp_attempt

    return rec(0, 0, set(), False)


if __name__ == "__main__":
    input = read("day08-01.txt")
    print(solve_1(input))  # 1594
    print(solve_2(input))  # 758
