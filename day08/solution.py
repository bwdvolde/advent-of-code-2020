from read_file.read_file import read_file


class Operation:

    def __init__(self, operation, sign, argument):
        self.operation = operation
        self.sign = sign
        self.argument = argument

    def __repr__(self):
        return f"{self.operation} {self.sign} {self.argument}"


def parse(lines):
    operations = []
    for line in lines:
        if not line:
            continue
        operation = line[:3]
        sign = line[4]
        argument = int(line[5:])
        operations.append(Operation(operation, sign, argument))

    return operations


def run_part_1(operations):
    i = 0
    acc = 0
    visited = set()
    while i not in visited:
        visited.add(i)
        operation = operations[i]
        if operation.operation == "nop":
            i += 1
        elif operation.operation == "acc":
            i += 1
            acc += operation.argument if operation.sign == "+" else -operation.argument
        else:
            i += operation.argument if operation.sign == "+" else -operation.argument

    return acc


def run_part_2(operations):
    i = 0
    acc = 0
    visited = set()
    while i not in visited and i < len(operations):
        visited.add(i)
        operation = operations[i]
        if operation.operation == "nop":
            i += 1
        elif operation.operation == "acc":
            i += 1
            acc += operation.argument if operation.sign == "+" else -operation.argument
        else:
            i += operation.argument if operation.sign == "+" else -operation.argument

    if i == len(operations):
        return acc, True
    return acc, False


if __name__ == '__main__':
    lines = read_file("input.txt")
    operations = parse(lines)

    acc = run_part_1(operations)
    print(f"Part 1: {acc}")

    acc = 0
    terminated = False
    j = 0
    while not terminated:
        operation = operations[j]
        if operation.operation == "jmp":
            operation.operation = "nop"
            acc, terminated = run_part_2(operations)
            operation.operation = "jmp"
        if operation.operation == "nop":
            operation.operation = "jmp"
            acc, terminated = run_part_2(operations)
            operation.operation = "nop"
        j += 1

    print(f"Part 2: {acc}")
