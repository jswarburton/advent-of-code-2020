from main.file_reader import read


def solve_1(input: list) -> int:
    return sum([solve(line) for line in input])


def solve_2(input: list) -> int:
    return sum([solve_advanced(line) for line in input])


def solve(equation: str) -> int:
    equation = equation.replace(" ", "")
    if "(" in equation:
        close_paren_idx = equation.find(")")
        open_paren_idx = equation[:close_paren_idx].rfind("(")
        inner = equation[open_paren_idx + 1 : close_paren_idx]
        sol = solve_no_paren(inner)
        new_equation = equation[:open_paren_idx] + str(sol) + equation[close_paren_idx + 1 :]
        return solve(new_equation)

    return solve_no_paren(equation)


def solve_advanced(equation: str) -> int:
    equation = equation.replace(" ", "")
    if "(" in equation:
        close_paren_idx = equation.find(")")
        open_paren_idx = equation[:close_paren_idx].rfind("(")
        inner = equation[open_paren_idx + 1 : close_paren_idx]
        inner_no_add = get_rid_of_add(inner)
        sol = solve_no_paren(inner_no_add)
        new_equation = equation[:open_paren_idx] + str(sol) + equation[close_paren_idx + 1 :]
        return solve_advanced(new_equation)

    equation_no_add = get_rid_of_add(equation)
    return solve_no_paren(equation_no_add)


def get_rid_of_add(equation: str) -> str:
    if "+" not in equation:
        return equation

    add_idx = equation.find("+")

    first = parse_last_thing(equation[:add_idx])
    second = parse_first_thing(equation[add_idx + 1 :])

    sol = int(first) + int(second)
    new_equation = (
        equation[: add_idx - len(first)] + str(sol) + equation[add_idx + len(second) + 1 :]
    )
    return get_rid_of_add(new_equation)


def solve_no_paren(equation: str) -> int:
    def rec(rem, total, operator) -> int:
        if not rem:
            return total

        c = parse_first_thing(rem)
        tail = rem[len(c) :]

        if c in ("+", "*"):
            return rec(tail, total, c)
        else:
            if operator == "+":
                return rec(tail, total + int(c), None)
            elif operator == "*":
                return rec(tail, total * int(c), None)
            else:
                return rec(tail, int(c), None)

    return rec(equation, 0, None)


def parse_first_thing(s: str) -> str:
    if s[0] in ("+", "*"):
        return s[0]
    else:
        for i, c in enumerate(s):
            if not c.isdigit():
                return s[:i]
        return s


def parse_last_thing(s: str) -> str:
    if s[0] in ("+", "*"):
        return s[0]
    else:
        for i in reversed(range(0, len(s))):
            if not s[i].isdigit():
                return s[i + 1 :]
        return s


if __name__ == "__main__":
    input = read("day18-01.txt")
    print(solve_1(input))  # 1408133923393
    print(solve_2(input))  # 314455761823725
