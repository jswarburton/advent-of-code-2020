from main.file_reader import read


def solve_1(input: list) -> int:
    memory = {}
    mask = ""

    for line in input:
        if line.startswith("mask = "):
            mask = line[7:]
        else:
            address, value = parse_address(line)
            memory[address] = apply_mask(value, mask)

    return sum(memory.values())


def parse_address(line: str) -> (int, int):
    first, num = line.split(" = ")
    return int(first.split("[")[1].split("]")[0]), int(num)


def apply_mask(value: int, mask: str) -> int:
    padded_value = "{0:b}".format(value).zfill(len(mask))
    masked_value = ""

    for (value_char, mask_char) in zip(padded_value, mask):
        if mask_char == "X":
            masked_value += value_char
        else:
            masked_value += mask_char

    return int(masked_value, 2)


def calculate_all_possibles(mask: str) -> list:
    possibles = []

    def rec(so_far, rem):
        if len(rem) == 0:
            possibles.append(so_far)
        else:
            if rem[0] == "X":
                rec(so_far + "1", rem[1:])
                rec(so_far + "0", rem[1:])
            else:
                rec(so_far + rem[0], rem[1:])

    rec("", mask)

    return possibles


def solve_2(input: list) -> int:
    memory = {}
    mask = ""

    for line in input:
        if line.startswith("mask = "):
            mask = line[7:]
        else:
            address, value = parse_address(line)

            masked_address = apply_mask_with_x(address, mask)
            all_possible_addresses = calculate_all_possibles(masked_address)

            for address in all_possible_addresses:
                memory[int(address, 2)] = value

    return sum(memory.values())


def apply_mask_with_x(value: int, mask: str) -> str:
    padded_value = "{0:b}".format(value).zfill(len(mask))
    masked_value = ""

    for (value_char, mask_char) in zip(padded_value, mask):
        if mask_char == "X" or mask_char == "1":
            masked_value += mask_char
        else:
            masked_value += value_char

    return masked_value


if __name__ == "__main__":
    input = read("day14-01.txt")
    print(solve_1(input))  # 7997531787333
    print(solve_2(input))  # 3564822193820
