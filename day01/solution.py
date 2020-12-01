from read_file.read_file import read_file


def part_1(entries):
    for i in range(len(entries)):
        for j in range(i, len(entries)):
            if entries[i] + entries[j] == 2020:
                return entries[i] * entries[j]


def part_2(entries):
    for i in range(len(entries)):
        for j in range(i, len(entries)):
            for k in range(j, len(entries)):
                if entries[i] + entries[j] + entries[k] == 2020:
                    return entries[i] * entries[j] * entries[k]


if __name__ == '__main__':
    lines = read_file("input.txt")
    entries = [int(line) for line in lines if line]

    print(f"Part 1: {part_1(entries)}")
    print(f"Part 2: {part_2(entries)}")
