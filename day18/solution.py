from read_file.read_file import read_file


def evaluate(expression):
    """
    >>> evaluate("1 + 2 * 3 + 4 * 5 + 6")
    71
    >>> evaluate("1 + (2 * 3) + (4 * (5 + 6))")
    51
    >>> evaluate("2 * 3 + (4 * 5)")
    26
    >>> evaluate("5 + (8 * 3 + 9 + 3 * 4 * 3)")
    437
    >>> evaluate("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")
    12240
    >>> evaluate("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")
    13632
    """
    current_value = 0
    current_op = None
    stack = []
    i = 0

    def process_number(number):
        nonlocal current_value, current_op
        if current_op:
            if current_op == "*":
                current_value *= number
            else:
                current_value += number
            current_op = None
        else:
            current_value = number

    while i < len(expression):
        c = expression[i]
        if c.isdigit():
            start_i = i
            i += 1
            while i < len(expression) and expression[i].isdigit():
                i += 1
            number = int(expression[start_i:i])
            process_number(number)
        elif c in ["+", "*"]:
            assert current_op is None
            current_op = c
            i += 1
        elif c == "(":
            stack.append((current_value, current_op))
            current_value, current_op = 0, None
            i += 1
        elif c == ")":
            number = current_value
            current_value, current_op = stack.pop()
            process_number(number)
            i += 1
        else:
            assert c == " "
            i += 1

    return current_value


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    expressions = read_file("input.txt")
    answer_part_1 = sum(evaluate(expression) for expression in expressions if expression)
    print(f"Part 1: {answer_part_1}")

