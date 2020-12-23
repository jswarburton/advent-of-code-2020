def solve_1(labeling: list, moves: int) -> str:
    linked = solve(labeling, moves)
    return "".join(str(i) for i in get_next_n(linked, 1, len(labeling) - 1))


def solve_2(labeling: list, num_cups: int, moves: int) -> str:
    labeling = [labeling[num] if num < len(labeling) else str(num + 1) for num in range(num_cups)]
    linked = solve(labeling, moves)
    return linked[1] * linked[linked[1]]


def solve(labeling, moves):
    labeling = [int(label) for label in labeling]
    num_cups = len(labeling)
    linked = {labeling[i]: labeling[(i + 1) % num_cups] for i in range(num_cups)}
    current = labeling[0]
    for _ in range(moves):
        pickups = get_next_n(linked, current, 3)
        destination = current - 1 if current > 1 else num_cups
        while destination in pickups:
            destination = destination - 1 if destination > 1 else num_cups

        linked[current] = linked[pickups[-1]]
        linked[pickups[-1]] = linked[destination]
        linked[destination] = pickups[0]

        current = linked[current]
    return linked


def get_next_n(after, current, n):
    next = []
    for _ in range(n):
        next.append(after[current])
        current = after[current]
    return next


if __name__ == "__main__":
    print(solve_1(list("952316487"), moves=100))  # 25398647
    print(solve_2(list("952316487"), num_cups=1_000_000, moves=10_000_000))  # 363807398885
