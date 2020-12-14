import re
from test.test_descrtut import defaultdict

from itertools import combinations

from read_file.read_file import read_file


def merge(bit, mask_bit):
    if mask_bit == "0":
        return bit
    return mask_bit


if __name__ == '__main__':
    lines = read_file("input.txt")

    mem = defaultdict(lambda: 0)

    mask_and, mask_or = None, None
    for line in lines:
        if not line:
            continue

        match = re.match("mask = (.*)", line)
        if match:
            mask = match.groups(1)[0]

        match = re.match("mem\[([0-9]+)] = ([0-9]+)", line)
        if match:
            address, value = map(int, match.groups(1))

            address_string = format(address, "036b")
            floating_memory_address_string = "".join(
                [bit if mask_bit == "0" else mask_bit for (bit, mask_bit) in zip(address_string, mask)])

            indexes = [i for (i, bit) in enumerate(floating_memory_address_string) if bit == "X"]
            for i in range(2 ** len(indexes)):
                binary_value = format(i, f"0{len(indexes)}b")


                def calculate_concrete_bit_value(j, bit):
                    if bit != "X":
                        return bit
                    assert (bit == "X")
                    return binary_value[indexes.index(j)]


                actual_memory_address_string = "".join(
                    [calculate_concrete_bit_value(j, bit) for j, bit in enumerate(floating_memory_address_string)])
                actual_memory_address = int(actual_memory_address_string, 2)
                mem[actual_memory_address] = value

    answer_part_2 = sum(mem.values())
    print(f"Part 2: {answer_part_2}")
