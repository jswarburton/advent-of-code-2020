from main.file_reader import read


def _calculate_row_id(code: str) -> int:
    row_part, column_part = code[:7], code[7:]

    row = _binary_search(row_part, 127, "B")
    column = _binary_search(column_part, 7, "R")

    return row * 8 + column


def _binary_search(code: str, val_max: int, top_char: str) -> int:
    current_min = 0
    current_max = val_max + 1
    for i in code:
        mid_point = (current_min + current_max) / 2
        if i == top_char:
            current_min = mid_point
        else:
            current_max = mid_point

    return current_max - 1


def find_highest_row_id(codes: list) -> int:
    row_ids = [int(_calculate_row_id(code)) for code in codes]
    return max(row_ids)


def find_missing_seat(codes: list) -> int:
    row_ids = {int(_calculate_row_id(code)) for code in codes}

    min_row_id = min(row_ids)
    max_row_id = max(row_ids)

    for i in range(min_row_id, max_row_id):
        if i not in row_ids:
            return i


if __name__ == "__main__":
    inputs = read("day05-01.txt")
    print(find_highest_row_id(inputs))  # 911
    print(find_missing_seat(inputs))  # 629
