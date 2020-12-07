from file_reader import read


def parse(line: str):
    colour, remainder = line.split(" bags contain ")
    remainder = remainder[:-1]  # remove trailing full stop

    children = {}

    if remainder != "no other bags":
        for child_part in remainder.split(", "):
            num_bags, rest = child_part.split(" ", 1)
            child_colour = rest.rsplit(" ", 1)[0]
            children[child_colour] = int(num_bags)
    return colour, children


def solve_1(input: list) -> int:
    full_dict = {}
    for line in input:
        colour, children = parse(line)
        full_dict[colour] = children

    bags_that_can_contain = set()

    def search(target):
        for colour, children in full_dict.items():
            if target in children:
                bags_that_can_contain.add(colour)
                search(colour)

    search("shiny gold")

    return len(bags_that_can_contain)


def solve_2(input: list) -> int:
    full_dict = {}
    for line in input:
        colour, children = parse(line)
        full_dict[colour] = children

    totals = []

    def search(target, multiplier):
        for colour, children in full_dict.items():
            if colour == target:
                for next_target in children.keys():
                    totals.append(multiplier * children[next_target])
                    search(next_target, multiplier * children[next_target])

    search("shiny gold", 1)

    return sum(totals)


if __name__ == "__main__":
    input = read("day07-01.txt")
    print(solve_1(input))  # 177
    print(solve_2(input))  # 34988
