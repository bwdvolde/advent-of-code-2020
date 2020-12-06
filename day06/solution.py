from read_file.read_file import read_file

if __name__ == '__main__':
    lines = read_file("input.txt")
    groups = []
    group = []
    for line in lines:
        if not line:
            groups.append(group)
            group = []
        else:
            group.append(line)

    count = sum(len({c for person in group for c in person}) for group in groups)
    print(f"Part 1: {count}")

    count = 0
    for group in groups:
        all_answered = set(group[0])
        for person in group:
            all_answered &= set(person)
        count += len(all_answered)

    print(f"Part 2: {count}")
