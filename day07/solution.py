import re

from collections import defaultdict

from read_file.read_file import read_file


class Bag:

    def __init__(self, name, contains):
        self.name = name
        self.contains = contains
        self.total_bags = sum(contain[0] for contain in contains)

    def __repr__(self):
        return f"{self.name} ({self.total_bags}): {self.contains}"


def parse(lines):
    bags = []
    for line in lines:
        if not line:
            continue
        name, contains_str = line.split(" contain ")
        # Remove the dot
        contains_str = contains_str[:-1]
        contains = []
        if contains_str != "no other bags":
            contained_bags_str = contains_str.split(", ")
            for contained_bag_str in contained_bags_str:
                match = re.match("^([0-9]) (.*)", contained_bag_str)
                count = int(match.groups(1)[0])
                bag_name = match.groups(1)[1]
                if bag_name[-4:] == "bags":
                    bag_name = bag_name[:-1]
                contains.append((count, bag_name))

        bags.append(Bag(name[:-1], contains))

    return bags


def part_1(bags):
    contained_in = defaultdict(lambda: [])
    for bag in bags:
        for contained_bag in bag.contains:
            bag_ = contained_bag[1]
            contained_in[bag_].append(bag.name)

    bags_containing_shiny_gold = set()
    stack = contained_in["shiny gold bag"]
    while stack:
        current = stack.pop()
        bags_containing_shiny_gold.add(current)
        for neighbour in contained_in[current]:
            if neighbour not in bags_containing_shiny_gold:
                stack.append(neighbour)
    return bags_containing_shiny_gold


if __name__ == '__main__':
    lines = read_file("input.txt")
    bags = parse(lines)

    bags_containing_shiny_gold = part_1(bags)
    print(f"Part 1: {len(bags_containing_shiny_gold)}")

    total_calculated = set(bag.name for bag in bags if not bag.contains)

    name_to_bag = {bag.name: bag for bag in bags}

    changed = True
    while changed:
        changed = False
        to_calculate_total = []

        for bag in bags:
            if bag.name not in total_calculated and all(contained[1] in total_calculated for contained in bag.contains):
                changed = True
                to_calculate_total.append(bag)

        for bag in to_calculate_total:
            bag.total_bags += sum(
                containing_bag[0] * name_to_bag[containing_bag[1]].total_bags for containing_bag in bag.contains)
            total_calculated.add(bag.name)

    print(name_to_bag["shiny gold bag"])
