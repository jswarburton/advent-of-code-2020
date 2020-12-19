import itertools

from main.file_reader import read


def calculate_possible_messages(n: str, rules: dict) -> set:
    cache = {}

    def rec(num: str) -> set:
        if num in cache:
            return cache[num]

        if '"' in rules[num]:
            possibles = {rules[num].replace('"', "")}
        else:
            if "|" in rules[num]:
                v1, v2 = rules[num].split(" | ", 1)

                parts_1 = v1.split(" ")
                sols_1 = [rec(part) for part in parts_1]
                possibles_1 = {"".join(s) for s in list(itertools.product(*sols_1))}

                parts_2 = v2.split(" ")
                sols_2 = [rec(part) for part in parts_2]
                possibles_2 = {"".join(s) for s in list(itertools.product(*sols_2))}

                possibles = possibles_1.union(possibles_2)
            else:
                parts = rules[num].split(" ")
                sols = [rec(part) for part in parts]

                possibles = {"".join(s) for s in list(itertools.product(*sols))}

        cache[num] = possibles
        return possibles

    return rec(n)


def solve_1(input: list) -> int:
    rules, messages = parse(input)
    possible_messages = calculate_possible_messages("0", rules)
    return sum(1 for message in messages if message in possible_messages)


def parse(input: list) -> (list, list):
    rules = {}
    messages = []

    is_messages = False
    for line in input:
        if not line:
            is_messages = True
            continue

        if is_messages:
            messages.append(line)
        else:
            rule_id, rule = line.split(": ")
            rules[rule_id] = rule

    return rules, messages


if __name__ == "__main__":
    input = read("day19-01.txt")
    print(solve_1(input))  # 220
