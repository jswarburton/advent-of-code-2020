from main.file_reader import read


def count_anyone_in_group_answer_yes(input: list) -> int:
    total = 0
    seen_in_group = set()
    for line in input:
        if not line:
            total += len(seen_in_group)
            seen_in_group = set()
        else:
            seen_in_group.update(list(line))

    total += len(seen_in_group)

    return total


def count_everyone_in_group_answer_yes(input: list) -> int:
    total = 0
    seen_in_group = set()
    new_group = True
    for line in input:
        if not line:
            total += len(seen_in_group)
            seen_in_group = set()
            new_group = True
        elif new_group:
            seen_in_group = set(line)
            new_group = False
        else:
            seen_in_group = seen_in_group.intersection(list(line))

    total += len(seen_in_group)

    return total


if __name__ == "__main__":
    input = read("day06-01.txt")
    print(count_anyone_in_group_answer_yes(input))  # 6714
    print(count_everyone_in_group_answer_yes(input))  # 3435
