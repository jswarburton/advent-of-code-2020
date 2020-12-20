from main.file_reader import read


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


def solve_2(input: list) -> int:
    return 2


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

    return grids


if __name__ == "__main__":
    input = read("day20-01.txt")
    print(solve_1(input))  # 4006801655873
    # print(solve_2(input))  #
