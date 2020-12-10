from collections import defaultdict
from functools import lru_cache

from read_file.read_file import read_file


def part_1(adapters):
    current_joltage = 0
    remaining_adapters = set(adapters)
    differences = defaultdict(lambda: 0)
    while remaining_adapters:
        for i in [1, 2, 3]:
            potential_adapter = current_joltage + i
            if potential_adapter in remaining_adapters:
                remaining_adapters.remove(potential_adapter)
                differences[i] += 1
                current_joltage += i
                break
    return differences[1] * (differences[3] + 1)


if __name__ == '__main__':
    lines = read_file("input.txt")
    adapters = [int(line) for line in lines if line]
    adapters.sort()

    answer_part_1 = part_1(adapters)
    print(f"Part 1: {answer_part_1}")

    combinations_map = defaultdict(lambda: 0)
    combinations_map[adapters[-1]] = 1
    for adapter in adapters[::-1][1:]:
        combinations_adapter = 0
        for i in [1, 2, 3]:
            combinations_adapter += combinations_map[adapter + i]

        combinations_map[adapter] = combinations_adapter

    answer_part_2 = sum(combinations_map[start_value] for start_value in [1, 2, 3])
    print(f"Part 2: {answer_part_2}")
