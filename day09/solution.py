from read_file.read_file import read_file


def has_2_sum(number, numbers):
    for i, number_a in enumerate(numbers):
        for _, number_b in enumerate(numbers, i + 1):
            if number == number_a + number_b:
                return True
    return False


if __name__ == '__main__':
    sliding_window = 25
    numbers = [int(line) for line in read_file("input.txt") if line]

    i = sliding_window + 1
    while has_2_sum(numbers[i], numbers[i - sliding_window:i]):
        i += 1

    answer_part_1 = numbers[i]
    print(f"Part 1: {answer_part_1}")

    count = 0
    start_i_in_range = 0
    start_i_not_in_range = 0
    while count != answer_part_1:
        if count + numbers[start_i_not_in_range] <= answer_part_1:
            count += numbers[start_i_not_in_range]
            start_i_not_in_range += 1
        else:
            count -= numbers[start_i_in_range]
            start_i_in_range += 1

    contiguous_range = numbers[start_i_in_range: start_i_not_in_range]
    answer_part_2 = min(contiguous_range) + max(contiguous_range)
    print(f"Part 2: {answer_part_2}")
