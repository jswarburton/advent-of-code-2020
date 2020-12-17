from main.file_reader import read


def solve_1(input: list) -> int:
    grid = [list(line) for line in input]
    active_cubes = set()

    num_iterations = 6

    initial_x_size, initial_y_size = len(grid[0]) - 1, len(grid) - 1

    for y in range(initial_y_size + 1):
        for x in range(initial_x_size + 1):
            if grid[y][x] == "#":
                active_cubes.add((x, y, 0))

    for i in range(1, num_iterations + 1):
        new_active_cubes = set()

        for y in range(-i, initial_y_size + i + 1):
            for x in range(-i, initial_x_size + i + 1):
                for z in range(-i, i + 1):

                    current_cube = (x, y, z)

                    surrounding_cubes = get_surrounding_3d(current_cube)
                    surrounding_active_cubes = surrounding_cubes.intersection(active_cubes)

                    if current_cube in active_cubes and len(surrounding_active_cubes) in [2, 3]:
                        new_active_cubes.add(current_cube)
                    elif len(surrounding_active_cubes) == 3:
                        new_active_cubes.add(current_cube)

        active_cubes = new_active_cubes

    return len(active_cubes)


def solve_2(input: list) -> int:
    grid = [list(line) for line in input]
    active_cubes = set()

    num_iterations = 6

    initial_x_size, initial_y_size = len(grid[0]) - 1, len(grid) - 1

    for y in range(initial_y_size + 1):
        for x in range(initial_x_size + 1):
            if grid[y][x] == "#":
                active_cubes.add((x, y, 0, 0))

    for i in range(1, num_iterations + 1):
        new_active_cubes = set()

        for y in range(-i, initial_y_size + i + 1):
            for x in range(-i, initial_x_size + i + 1):
                for z in range(-i, i + 1):
                    for w in range(-i, i + 1):

                        current_cube = (x, y, z, w)

                        surrounding_cubes = get_surrounding_4d(current_cube)
                        surrounding_active_cubes = surrounding_cubes.intersection(active_cubes)

                        if current_cube in active_cubes and len(surrounding_active_cubes) in [2, 3]:
                            new_active_cubes.add(current_cube)
                        elif len(surrounding_active_cubes) == 3:
                            new_active_cubes.add(current_cube)

        active_cubes = new_active_cubes

    return len(active_cubes)


def get_surrounding_3d(coord) -> set:
    x, y, z = coord

    surrounding = set()

    for x1 in range(x - 1, x + 2):
        for y1 in range(y - 1, y + 2):
            for z1 in range(z - 1, z + 2):
                surrounding.add((x1, y1, z1))
    surrounding.remove(coord)
    return surrounding


def get_surrounding_4d(coord) -> set:
    x, y, z, w = coord

    surrounding = set()

    for x1 in range(x - 1, x + 2):
        for y1 in range(y - 1, y + 2):
            for z1 in range(z - 1, z + 2):
                for w1 in range(w - 1, w + 2):
                    surrounding.add((x1, y1, z1, w1))
    surrounding.remove(coord)
    return surrounding


if __name__ == "__main__":
    input = read("day17-01.txt")
    print(solve_1(input))  # 304
    print(solve_2(input))  # 1868
