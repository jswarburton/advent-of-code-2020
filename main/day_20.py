import math
from collections import defaultdict

from main.file_reader import read

sea_monster = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]


def solve_1(input: list) -> int:
    grids = parse(input)

    grid_id_to_edge_signatures = {
        grid_id: grid_edge_signatures(grid) for grid_id, grid in grids.items()
    }

    corner_pieces = find_corner_pieces(grid_id_to_edge_signatures)

    total = 1
    for id in corner_pieces:
        total *= id
    return total


def grid_edge_signatures(grid: list) -> (set, set):
    standard_sigs = {
        grid[0],
        grid[-1],
        "".join([row[0] for row in grid]),
        "".join([row[-1] for row in grid]),
    }
    flipped_sigs = {sig[::-1] for sig in standard_sigs}
    return (standard_sigs, flipped_sigs)


def find_corner_pieces(grid_id_to_edge_signatures: dict) -> set:
    corner_pieces = set()
    for grid_id, (edge_signatures, flipped_edge_signatures) in grid_id_to_edge_signatures.items():
        all_others = set()
        for other_grid_id, (
            other_edge_signatures,
            other_flipped_edge_signatures,
        ) in grid_id_to_edge_signatures.items():
            if other_grid_id != grid_id:
                all_others = all_others.union(other_edge_signatures).union(
                    other_flipped_edge_signatures
                )

        num_unique_regular = sum(1 for sig in edge_signatures if sig not in all_others)
        num_unique_flipped = sum(1 for sig in flipped_edge_signatures if sig not in all_others)

        if num_unique_regular == 2 or num_unique_flipped == 2:
            corner_pieces.add(grid_id)

    assert len(corner_pieces) == 4
    return corner_pieces


def solve_2(input: list) -> int:
    tiles = parse(input)
    grid = generate_grid(tiles)
    num_sea_monsters = max(find_sea_monsters(grid) for grid in all_permutations(grid))
    num_hash_per_sea_monster = sum(row.count("#") for row in sea_monster)
    return sum(row.count("#") for row in grid) - (num_sea_monsters * num_hash_per_sea_monster)


def all_permutations(grid: list) -> list:
    def all_rotations(grid: list) -> list:
        return [
            grid,
            rotate(grid),
            rotate(rotate(grid)),
            rotate(rotate(rotate(grid))),
        ]

    return (
        all_rotations(grid)
        + all_rotations(reflect_vertical(grid))
        + all_rotations(reflect_horizontal(grid))
    )


def find_sea_monsters(grid: list) -> int:
    count = 0

    monster_signature = {
        (row_num, col_num)
        for row_num, row in enumerate(sea_monster)
        for col_num, elem in enumerate(row)
        if elem == "#"
    }

    max_row, max_col = max(row for row, col in monster_signature), max(
        col for row, col in monster_signature
    )

    for i, row in enumerate(grid[:-max_row]):
        for j, elem in enumerate(row[:-max_col]):
            if all(
                grid[i + monster_row][j + monster_col] == "#"
                for (monster_row, monster_col) in monster_signature
            ):
                count += 1

    return count


def generate_grid(tiles: dict) -> list:
    width = int(math.sqrt(len(tiles)))
    all_possible_grids = build_all_possible_grids(tiles)

    graph = find_connected_grids(all_possible_grids)
    tiles = {title: grid for (title, grid, _, _) in all_possible_grids}
    corners = [k for k, v in graph.items() if len(v) == 2]

    pattern = next(
        dfs(corner, tiles, graph, width) for corner in corners if dfs(corner, tiles, graph, width)
    )

    chunked = [
        pattern[i * width : (i + 1) * width] for i in range((len(pattern) + width - 1) // width)
    ]
    full_representation = [[crop(tiles[title]) for title in titles] for titles in chunked]

    return [
        "".join([block[i] for block in blocks])
        for blocks in full_representation
        for i in range(len(blocks[0]))
    ]


def parse(input: list) -> dict:
    grids = {}

    grid_id = None
    current_grid = []

    for line in input:
        if not line:
            grids[grid_id] = current_grid
            current_grid = []
        elif "Tile " in line:
            grid_id = int(line[5:-1])
        else:
            current_grid.append(line)

    grids[grid_id] = current_grid
    return grids


def reflect_vertical(grid):
    return grid[::-1]


def reflect_horizontal(grid):
    return [a[::-1] for a in grid]


def rotate(grid):
    return ["".join(row) for row in list(zip(*grid[::-1]))]


def crop(grid):
    return [row[1:-1] for row in grid[1:-1]]


def row(tile_num, operation, grid):
    t = "{}:{}".format(tile_num, operation)
    return (t, grid, tile_num, hash_grid(grid))


def build_all_possible_grids(tiles):
    grids = []
    for tile_num, grid in tiles.items():
        grids += [
            row(tile_num, "standard", grid),
            row(tile_num, "reflect-vertical", reflect_vertical(grid)),
            row(tile_num, "reflect-horizontal", reflect_horizontal(grid)),
            row(
                tile_num,
                "reflect-vertical:reflect-horizontal",
                reflect_vertical(reflect_horizontal(grid)),
            ),
            row(tile_num, "rotated", rotate(grid)),
            row(tile_num, "reflect-horizontal:rotated", reflect_horizontal(rotate(grid))),
            row(tile_num, "reflect-vertical:rotated", reflect_vertical(rotate(grid))),
        ]
    return grids


def hash_grid(g):
    rg = rotate(g)
    return [hash("".join(gr)) for gr in [g[0], g[-1], rg[0], rg[-1]]]


def valign(box1, box2):
    return box1[-1] == box2[0]


def halign(box1, box2):
    for i in range(len(box1)):
        if not box1[i][-1] == box2[i][0]:
            return False
    return True


def connected(tile_num_1, hash1, tile_num_2, hash2):
    return (tile_num_1 != tile_num_2) and (
        hash1[0] == hash2[1] or hash1[1] == hash2[0] or hash1[2] == hash2[3] or hash1[3] == hash2[2]
    )


def connect(list, a1, a2):
    list[a1].append(a2)
    list[a2].append(a1)


def find_connected_grids(all_grids):
    candidates = defaultdict(list)
    [
        connect(candidates, k1, k2)
        for i, (k1, _, l1, h1) in enumerate(all_grids)
        for k2, _, l2, h2 in all_grids[i:]
        if connected(l1, h1, l2, h2)
    ]
    return candidates


def is_complete(x, y, w):
    return y == w - 1 and ((y % 2 == 0 and x == w - 1) or (y % 2 == 1 and x == 0))


def aligns(g1, x1, y1, g2, x2, y2):
    if x1 == x2:
        return valign(g1, g2) if y1 < y2 else valign(g2, g1)
    if y1 == y2:
        return halign(g1, g2) if x1 < x2 else halign(g2, g1)


def next_option(x, y, width):
    if (x == width - 1 and y % 2 == 0) or (x == 0 and y % 2 == 1):
        y += 1
        x = -1 if y % 2 == 0 else width
    x = x + 1 if y % 2 == 0 else x - 1
    return (x, y)


def dfs(start, grids, candidates, width):
    grid = [0 for _ in range(width ** 2)]

    grid[0] = start
    q = [(grid, start, 0, 0)]

    visited = set()

    while q:
        grid, last, x, y = q.pop()

        if is_complete(x, y, width):
            return grid
        if tuple(grid) in visited:
            continue
        visited.add(tuple(grid))

        xx, yy = next_option(x, y, width)
        for c in candidates[last]:
            if c not in grid and aligns(grids[last], x, y, grids[c], xx, yy):
                grid = grid[:]
                grid[yy * width + xx] = c
                q.append((grid, c, xx, yy))

    return None


if __name__ == "__main__":
    input = read("day20-01.txt")
    print(solve_1(input), 4006801655873)
    print(solve_2(input), 1838)
