from read_file.read_file import read_file


def evaluate(expression):
    """
    >>> evaluate("1 + 2 * 3 + 4 * 5 + 6")
    '231'
    >>> evaluate("1 + (2 * 3) + (4 * (5 + 6))")
    '51'
    >>> evaluate("2 * 3 + (4 * 5)")
    '46'
    >>> evaluate("5 + (8 * 3 + 9 + 3 * 4 * 3)")
    '1445'
    >>> evaluate("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")
    '669060'
    >>> evaluate("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")
    '23340'
    """
    if expression.isdigit():
        return expression

    # Evaluate subexpressions between parentheses
    rewritten_expression = ""
    i = 0
    while i < len(expression):
        if expression[i] == "(":
            level = 1
            j = i
            while not (level == 0 and expression[j] == ")"):
                j += 1
                if expression[j] == ")":
                    level -= 1
                elif expression[j] == "(":
                    level += 1

            rewritten_expression += evaluate(expression[i + 1: j])
            i = j + 1
        else:
            rewritten_expression += expression[i]
            i += 1

    expression = rewritten_expression
    index_of_operator = expression.find("*")
    if index_of_operator == -1:
        index_of_operator = expression.find("+")

    left = evaluate(expression[:index_of_operator - 1])
    right = evaluate(expression[index_of_operator + 2:])

    if expression[index_of_operator] == "*":
        return str(int(left) * int(right))
    else:
        return str(int(left) + int(right))


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    expressions = read_file("input.txt")
    answer_part_2 = sum(int(evaluate(expression)) for expression in expressions if expression)
    print(f"Part 2: {answer_part_2}")
