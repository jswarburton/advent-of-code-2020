from main.file_reader import read


def solve_1(input: list) -> int:
    parsed = parse(input)

    all_allergens = set()
    for ingredients, allergens in parsed:
        all_allergens = all_allergens.union(allergens)

    allergen_to_maybes = {}
    for allergen in all_allergens:
        maybes = set()
        for ingredients, allergens in parsed:
            if allergen in allergens:
                if maybes:
                    maybes = maybes.intersection(ingredients)
                else:
                    maybes = maybes.union(ingredients)
        allergen_to_maybes[allergen] = maybes

    all_maybes = set()
    for allergen, maybes in allergen_to_maybes.items():
        all_maybes = all_maybes.union(maybes)

    ingredients_with_no_allergens = set()
    for ingredients, allergens in parsed:
        for ingredient in ingredients:
            if ingredient not in all_maybes:
                ingredients_with_no_allergens.add(ingredient)

    appearances = 0
    for ingredients, allergens in parsed:
        appearances += len(ingredients.intersection(ingredients_with_no_allergens))
    return appearances


def solve_2(input: list) -> str:
    parsed = parse(input)

    all_allergens = set()
    for ingredients, allergens in parsed:
        all_allergens = all_allergens.union(allergens)

    allergen_to_maybes = {}
    for allergen in all_allergens:
        maybes = set()
        for ingredients, allergens in parsed:
            if allergen in allergens:
                if maybes:
                    maybes = maybes.intersection(ingredients)
                else:
                    maybes = maybes.union(ingredients)
        allergen_to_maybes[allergen] = maybes

    while any([len(v) > 1 for v in allergen_to_maybes.values()]):
        for v in allergen_to_maybes.values():
            if len(v) == 1:
                for k, v_inner in allergen_to_maybes.items():
                    if len(v_inner) > 1 and list(v)[0] in v_inner:
                        v_inner.remove(list(v)[0])

    allergen_to_ingredient = {k: list(v)[0] for k, v in allergen_to_maybes.items()}
    alphabetical_allergens = list(allergen_to_ingredient.keys())
    alphabetical_allergens.sort()

    return ",".join([allergen_to_ingredient[a] for a in alphabetical_allergens])


def parse(input: list) -> list:
    parsed = []
    for line in input:
        ingredients, allergens = line.split(" (contains ")

        ingredients = set(ingredients.split(" "))
        allergens = set(allergens[:-1].split(", "))

        parsed.append((ingredients, allergens))
    return parsed


if __name__ == "__main__":
    input = read("day21-01.txt")
    print(solve_1(input))  # 2826
    print(solve_2(input))  # "pbhthx,sqdsxhb,dgvqv,csnfnl,dnlsjr,xzb,lkdg,rsvlb"
