import re

from collections import defaultdict

from read_file.read_file import read_file


def parse():
    lines = read_file("input.txt")

    fields = {}
    tickets = []

    iterator = iter(lines)
    while line := next(iterator):
        field, *ranges = re.match("(.+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)", line).groups()
        ranges = list(map(int, ranges))
        fields[field] = [tuple(ranges[:2]), tuple(ranges[2:])]

    # Skip your ticket:
    next(iterator)

    my_ticket = next(iterator)
    my_ticket = my_ticket.split(",")
    my_ticket = list(map(int, my_ticket))

    # Skip empty line and nearby tickets:
    next(iterator)
    next(iterator)
    while line := next(iterator):
        ticket = line
        ticket = ticket.split(",")
        ticket = list(map(int, ticket))
        tickets.append(ticket)

    return fields, my_ticket, tickets


def calculate_error_rate(fields, tickets):
    all_ranges = [range for ranges in fields.values() for range in ranges]
    indexes_to_discard = set()
    error_rate = 0
    for i, ticket in enumerate(tickets):
        for value in ticket:
            if all(not lower <= value <= upper for (lower, upper) in all_ranges):
                error_rate += value
                indexes_to_discard.add(i)
    return error_rate, indexes_to_discard


if __name__ == '__main__':
    fields, my_ticket, tickets = parse()

    error_rate, indexes_to_discard = calculate_error_rate(fields, tickets)
    tickets = [ticket for i, ticket in enumerate(tickets) if i not in indexes_to_discard]
    print(f"Part 1: {error_rate}")

    valid_fields_for_index = defaultdict(lambda: [])

    tickets.append(my_ticket)
    for index in range(len(my_ticket)):
        for field, ranges in fields.items():
            valid_field = True
            for ticket in tickets:
                ticket_value = ticket[index]
                if not (ranges[0][0] <= ticket_value <= ranges[0][1] or ranges[1][0] <= ticket_value <= ranges[1][1]):
                    valid_field = False
            if valid_field:
                valid_fields_for_index[index].append(field)

    field_assigned_to = {}
    assign_order = list(sorted([index for index in valid_fields_for_index.keys()], key=lambda index: len(valid_fields_for_index[index])))
    for index in assign_order:
        remaining_assignable_fields = [field for field in valid_fields_for_index[index] if field not in field_assigned_to.keys()]
        assert len(remaining_assignable_fields) == 1
        field_to_assign = remaining_assignable_fields[0]
        field_assigned_to[field_to_assign] = index

    answer_part_2 = 1
    for field, index in field_assigned_to.items():
        if field.startswith("departure"):
            answer_part_2 *= my_ticket[index]
    print(f"Part 2: {answer_part_2}")





