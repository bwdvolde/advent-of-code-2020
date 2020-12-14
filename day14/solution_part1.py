import re
from test.test_descrtut import defaultdict

from read_file.read_file import read_file

if __name__ == '__main__':
    lines = read_file("input.txt")

    mem = defaultdict(lambda : 0)

    mask_and, mask_or = None, None
    for line in lines:
        if not line:
            continue

        match = re.match("mask = (.*)", line)
        if match:
            mask = match.groups(1)[0]
            mask_and = int(mask.replace("X", "1"), 2)
            mask_or = int(mask.replace("X", "0"), 2)

        match = re.match("mem\[([0-9]+)] = ([0-9]+)", line)
        if match:
            address, value = map(int, match.groups(1))
            masked_value = value & mask_and | mask_or
            mem[address] = masked_value

    answer_part_1 = sum(mem.values())
    print(f"Part 1: {answer_part_1}")
