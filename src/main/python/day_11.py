from file_reader import read


def copy_grid(grid):
    new_grid = []
    for line in grid:
        new_grid.append(line.copy())
    return new_grid


def solve_1(input: list) -> int:
    grid = [list(line) for line in input]

    num_rows = len(grid)
    num_cols = len(grid[0])

    while True:
        new_grid = copy_grid(grid)

        for row in range(num_rows):
            for col in range(num_cols):
                num_adjacent_occupied = 0
                if row - 1 >= 0 and grid[row - 1][col] == "#":
                    num_adjacent_occupied += 1
                if row - 1 >= 0 and col - 1 >= 0 and grid[row - 1][col - 1] == "#":
                    num_adjacent_occupied += 1
                if row - 1 >= 0 and col + 1 < num_cols and grid[row - 1][col + 1] == "#":
                    num_adjacent_occupied += 1

                if row + 1 < num_rows and grid[row + 1][col] == "#":
                    num_adjacent_occupied += 1
                if row + 1 < num_rows and col - 1 >= 0 and grid[row + 1][col - 1] == "#":
                    num_adjacent_occupied += 1
                if row + 1 < num_rows and col + 1 < num_cols and grid[row + 1][col + 1] == "#":
                    num_adjacent_occupied += 1

                if col - 1 >= 0 and grid[row][col - 1] == "#":
                    num_adjacent_occupied += 1
                if col + 1 < num_cols and grid[row][col + 1] == "#":
                    num_adjacent_occupied += 1

                if grid[row][col] == "L" and num_adjacent_occupied == 0:
                    new_grid[row][col] = "#"
                elif grid[row][col] == "#" and num_adjacent_occupied >= 4:
                    new_grid[row][col] = "L"

        if new_grid == grid:
            grid = new_grid
            break
        grid = new_grid

    return sum([row.count("#") for row in grid])


def solve_2(input: list) -> int:
    grid = [list(line) for line in input]

    num_rows = len(grid)
    num_cols = len(grid[0])

    while True:
        new_grid = copy_grid(grid)

        for row in range(num_rows):
            for col in range(num_cols):
                num_adjacent_occupied = 0

                # UP
                row_to_check = row - 1
                while row_to_check >= 0:
                    if grid[row_to_check][col] == "#":
                        num_adjacent_occupied += 1
                        break
                    elif grid[row_to_check][col] == "L":
                        break
                    row_to_check -= 1

                # DOWN
                row_to_check = row + 1
                while row_to_check < num_rows:
                    if grid[row_to_check][col] == "#":
                        num_adjacent_occupied += 1
                        break
                    elif grid[row_to_check][col] == "L":
                        break
                    row_to_check += 1

                # LEFT
                col_to_check = col - 1
                while col_to_check >= 0:
                    if grid[row][col_to_check] == "#":
                        num_adjacent_occupied += 1
                        break
                    elif grid[row][col_to_check] == "L":
                        break
                    col_to_check -= 1

                # RIGHT
                col_to_check = col + 1
                while col_to_check < num_cols:
                    if grid[row][col_to_check] == "#":
                        num_adjacent_occupied += 1
                        break
                    elif grid[row][col_to_check] == "L":
                        break
                    col_to_check += 1

                # LEFT UP
                row_to_check = row - 1
                col_to_check = col - 1
                while col_to_check >= 0 and row_to_check >= 0:
                    if grid[row_to_check][col_to_check] == "#":
                        num_adjacent_occupied += 1
                        break
                    elif grid[row_to_check][col_to_check] == "L":
                        break
                    row_to_check -= 1
                    col_to_check -= 1

                # RIGHT UP
                row_to_check = row - 1
                col_to_check = col + 1
                while col_to_check < num_cols and row_to_check >= 0:
                    if grid[row_to_check][col_to_check] == "#":
                        num_adjacent_occupied += 1
                        break
                    elif grid[row_to_check][col_to_check] == "L":
                        break
                    row_to_check -= 1
                    col_to_check += 1

                # LEFT DOWN
                row_to_check = row + 1
                col_to_check = col - 1
                while col_to_check >= 0 and row_to_check < num_rows:
                    if grid[row_to_check][col_to_check] == "#":
                        num_adjacent_occupied += 1
                        break
                    elif grid[row_to_check][col_to_check] == "L":
                        break
                    row_to_check += 1
                    col_to_check -= 1

                # RIGHT DOWN
                row_to_check = row + 1
                col_to_check = col + 1
                while col_to_check < num_cols and row_to_check < num_rows:
                    if grid[row_to_check][col_to_check] == "#":
                        num_adjacent_occupied += 1
                        break
                    elif grid[row_to_check][col_to_check] == "L":
                        break
                    row_to_check += 1
                    col_to_check += 1

                if grid[row][col] == "L" and num_adjacent_occupied == 0:
                    new_grid[row][col] = "#"
                elif grid[row][col] == "#" and num_adjacent_occupied >= 5:
                    new_grid[row][col] = "L"

        if new_grid == grid:
            grid = new_grid
            break
        grid = new_grid

    return sum([row.count("#") for row in grid])


def print_grid(grid):
    num_rows = len(grid)
    for row in range(num_rows):
        print(grid[row])
    print()


if __name__ == "__main__":
    grid = read("day11-01.txt")
    print(solve_1(grid))  # 2470
    print(solve_2(grid))  # 2259
