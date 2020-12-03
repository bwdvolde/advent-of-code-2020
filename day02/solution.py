import re
from read_file.read_file import read_file


class Entry:

    def __init__(self, lower_bound, upper_bound, letter, password):
        self.lower_bound = int(lower_bound)
        self.upper_bound = int(upper_bound)
        self.letter = letter
        self.password = password


def is_valid_part_1(entry):
    count = sum(1 for c in entry.password if c == entry.letter)
    return entry.lower_bound <= count <= entry.upper_bound

def is_valid_part_2(entry):
    count = sum(1 for i in [entry.lower_bound - 1, entry.upper_bound - 1] if entry.password[i] == entry.letter)
    return count == 1

if __name__ == '__main__':
    lines = read_file("input.txt")

    entries = []
    for line in lines:
        if line != "":
            match = re.match("(.*)-(.*) (.): (.*)", line)
            entry = Entry(*match.groups())
            # print(entry.letter)
            entries.append(entry)

    part_1_answer = sum(is_valid_part_1(entry) for entry in entries)
    print(f"Part 1: {part_1_answer}")

    part_2_answer = sum(is_valid_part_2(entry) for entry in entries)
    print(f"Part 2: {part_2_answer}")
