from main.file_reader import read


def solve_1(input: list) -> int:
    parsed = [parse(line) for line in input]

    black_tiles = set()

    for instructions in parsed:
        tile = find_tile(instructions)

        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)

    return len(black_tiles)


def solve_2(input: list) -> int:
    parsed = [parse(line) for line in input]

    black_tiles = set()

    for instructions in parsed:
        tile = find_tile(instructions)

        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)

    for _ in range(100):
        min_x = min(x for x, y in black_tiles)
        max_x = max(x for x, y in black_tiles)
        min_y = min(y for x, y in black_tiles)
        max_y = max(y for x, y in black_tiles)

        new_black_tiles = set()

        for x in range(min_x - 1, max_x + 2):
            for y in range(min_y - 1, max_y + 2):
                tile = (x, y)
                surrounding = surrounding_tiles(tile)
                surrounding_black = black_tiles.intersection(surrounding)

                if tile not in black_tiles and len(surrounding_black) == 2:
                    new_black_tiles.add(tile)
                elif tile in black_tiles and len(surrounding_black) in (1, 2):
                    new_black_tiles.add(tile)

        black_tiles = new_black_tiles

    return len(black_tiles)


def find_tile(instructions: list, starting_point=(0, 0)) -> (int, int):
    x, y = starting_point
    for instruction in instructions:
        if instruction == "e":
            x += 1
        elif instruction == "se":
            if y % 2 == 0:
                x += 1
            y += 1
        elif instruction == "sw":
            if y % 2 != 0:
                x -= 1
            y += 1
        elif instruction == "w":
            x -= 1
        elif instruction == "nw":
            if y % 2 != 0:
                x -= 1
            y -= 1
        elif instruction == "ne":
            if y % 2 == 0:
                x += 1
            y -= 1
        else:
            raise Exception
    return x, y


def surrounding_tiles(tile: (int, int)) -> set:
    directions = ["e", "se", "sw", "w", "nw", "ne"]
    return {find_tile([direction], tile) for direction in directions}


def parse(line: str) -> list:
    i = 0
    output = []
    while i < len(line):
        c = line[i]
        if c in ("e", "w"):
            output.append(c)
            i += 1
        else:
            output.append(line[i : i + 2])
            i += 2
    return output


if __name__ == "__main__":
    input = read("day24-01.txt")
    print(solve_1(input))  # 244
    print(solve_2(input))  # 3665
