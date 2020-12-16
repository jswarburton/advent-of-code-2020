from main.file_reader import read


def solve_1(input: list) -> int:
    my_ticket, nearby_tickets, departure_idxs, ranges = parse(input)

    invalid_values = [field for field in my_ticket if not in_ranges(field, ranges)]

    for nearby_ticket in nearby_tickets:
        for field in nearby_ticket:
            if not in_ranges(field, ranges):
                invalid_values.append(field)

    return sum(invalid_values)


def in_ranges(num: int, ranges: list) -> bool:
    return any(in_specific_ranges(num, specific_ranges) for specific_ranges in ranges)


def in_specific_ranges(num: int, specific_ranges: list) -> bool:
    range1, range2 = specific_ranges
    return (num >= range1[0] and num <= range1[1]) or (num >= range2[0] and num <= range2[1])


def solve_2(input: list) -> int:
    my_ticket, nearby_tickets, departure_idxs, ranges = parse(input)

    valid_tickets = [
        nearby_ticket
        for nearby_ticket in nearby_tickets
        if all(in_ranges(field, ranges) for field in nearby_ticket)
    ]

    ticket_field_to_valid_ranges = {}
    for ticket_field_idx in range(len(valid_tickets[0]) - 1):
        for range_idx, two_ranges in enumerate(ranges):
            if all(
                in_specific_ranges(ticket[ticket_field_idx], two_ranges) for ticket in valid_tickets
            ):
                if ticket_field_idx in ticket_field_to_valid_ranges:
                    ticket_field_to_valid_ranges[ticket_field_idx].append(range_idx)
                else:
                    ticket_field_to_valid_ranges[ticket_field_idx] = [range_idx]

    # TODO this is a bit hacky - it can't resolve the last few but they aren't important
    for i in range(len(ranges)):
        removables = [
            valid_ranges[0]
            for valid_ranges in ticket_field_to_valid_ranges.values()
            if len(valid_ranges) == 1
        ]
        for valid_ranges in ticket_field_to_valid_ranges.values():
            if len(valid_ranges) != 1:
                for removable in removables:
                    if removable in valid_ranges:
                        valid_ranges.remove(removable)

    flipped_idx = {v[0]: k for (k, v) in ticket_field_to_valid_ranges.items()}

    product = 1
    for i in [flipped_idx[i] for i in departure_idxs]:
        product *= my_ticket[i]

    return product


def parse(input):
    ranges = []
    departure_idxs = []
    my_ticket = []
    nearby_tickets = []

    your_ticket_flag, nearby_tickets_flag = False, False

    for line in input:
        if not line:
            pass
        elif " or " in line:
            text, range_part = line.split(": ", 1)
            range1, range2 = range_part.split(" or ", 1)

            r1_min, r1_max = range1.split("-")
            r2_min, r2_max = range2.split("-")

            if "departure" in line:
                departure_idxs.append(len(ranges))
            ranges.append([(int(r1_min), int(r1_max)), (int(r2_min), int(r2_max))])
        elif "your ticket:" in line:
            your_ticket_flag = True
        elif your_ticket_flag:
            my_ticket = [int(n) for n in line.split(",")]
            your_ticket_flag = False
        elif "nearby tickets:" in line:
            nearby_tickets_flag = True
        elif nearby_tickets_flag:
            nearby_tickets.append([int(n) for n in line.split(",")])
    return my_ticket, nearby_tickets, departure_idxs, ranges


if __name__ == "__main__":
    input = read("day16-01.txt")
    print(solve_1(input))  # 23036
    print(solve_2(input))  # 1909224687553
