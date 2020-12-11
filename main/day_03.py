from main.file_reader import read


def count_trees_hit(lines: list, right_gradient: int, down_gradient: int) -> int:
    height = len(lines)
    width = len(lines[0])

    right = 0
    down = 0

    num_trees_hit = 0

    while True:
        if down >= height:
            return num_trees_hit

        if lines[down][right] == "#":
            num_trees_hit = num_trees_hit + 1

        right = (right + right_gradient) % width
        down = down + down_gradient


def product_trees_hit(lines: list, gradients: list) -> int:
    num_trees = [
        count_trees_hit(lines, right_gradient=gradient[0], down_gradient=gradient[1])
        for gradient in gradients
    ]

    product = 1
    for num in num_trees:
        product = product * num

    return product


if __name__ == "__main__":
    input = read("day03-01.txt")
    print(count_trees_hit(input, right_gradient=3, down_gradient=1))

    gradients = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    print(product_trees_hit(input, gradients))
