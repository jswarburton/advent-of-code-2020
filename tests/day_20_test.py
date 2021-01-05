from main import file_reader
from main.day_20 import all_permutations, find_sea_monsters, generate_grid, parse, solve_1, solve_2

input = file_reader.read(file_name="day_20_test_input.txt", path="tests/resources")
expected_grid = file_reader.read(file_name="day_20_expected_grid.txt", path="tests/resources")


def test_solve_1():
    assert solve_1(input) == 20899048083289


def test_find_sea_monsters():
    grid = [
        ".#.#..#.##...#.##..#####",
        "###....#.#....#..#......",
        "##.##.###.#.#..######...",
        "###.#####...#.#####.#..#",
        "##.#....#.##.####...#.##",
        "...########.#....#####.#",
        "....#..#...##..#.#.###..",
        ".####...#..#.....#......",
        "#..#.##..#..###.#.##....",
        "#.####..#.####.#.#.###..",
        "###.#.#...#.######.#..##",
        "#.####....##..########.#",
        "##..##.#...#...#.#.#.#..",
        "...#..#..#.#.##..###.###",
        ".#.#....#.##.#...###.##.",
        "###.#...#..#.##.######..",
        ".#.#.###.##.##.#..#.##..",
        ".####.###.#...###.#..#.#",
        "..#.#..#..#.#.#.####.###",
        "#..####...#.#.#.###.###.",
        "#####..#####...###....##",
        "#.##..#..#...#..####...#",
        ".#.###..##..##..####.##.",
        "...###...##...#...#..###",
    ]

    assert max(find_sea_monsters(grid) for grid in all_permutations(grid)) == 2


def test_generate_grid():
    tiles = parse(input)
    assert generate_grid(tiles) in all_permutations(expected_grid)


def test_solve_2():
    assert solve_2(input) == 273
