from day_03 import count_trees_hit, product_trees_hit

input = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]


def test_single_gradient():
    assert count_trees_hit(input, right_gradient=3, down_gradient=1) == 7


def test_multiple_gradients():
    gradients = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    assert product_trees_hit(input, gradients) == 336
