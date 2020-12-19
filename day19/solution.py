import re
from functools import lru_cache

from read_file.read_file import read_file

if __name__ == '__main__':
    lines = read_file("input.txt")

    iterator = iter(lines)

    rules = {}
    while line := next(iterator):
        rule_id, rule = line.split(": ")
        rules[rule_id] = rule

    messages = list(iterator)
    messages = [message for message in messages if message]

    @lru_cache
    def calculate_regex_part_1(rule_id):
        rule = rules[rule_id]
        if re.match("\"[a-b]\"", rule):
            return rule[1]
        tokens = rule.split(" ")
        return "".join(token if token == "|" else f"({calculate_regex_part_1(token)})" for token in tokens)


    def find_matches(regex):
        return sum(1 for message in messages if re.match(regex, message))

    regex_part_1 = f"^{calculate_regex_part_1('0')}$"
    print(f"Part 1: {find_matches(regex_part_1)}")

    regex_part_42 = calculate_regex_part_1("42")
    regex_part_31 = calculate_regex_part_1("31")

    print(regex_part_42)
    regex = f"^({regex_part_42}){{2,}}({regex_part_31})+$"

    # for message in messages:
    #     if re.match(regex, message):
    #         print(message)
