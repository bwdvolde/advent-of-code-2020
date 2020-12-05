from read_file.read_file import read_file


def calculate_row(seat):
    row_str = seat[:7]
    in_binary = row_str.replace("F", "0").replace("B", "1")
    return int(in_binary, 2)


def calculate_col(seat):
    col_str = seat[7:]
    in_binary = col_str.replace("L", "0").replace("R", "1")
    return int(in_binary, 2)


def calculate_seat_id(seat):
    return 8 * calculate_row(seat) + calculate_col(seat)


if __name__ == '__main__':
    seats = read_file("input.txt")[:-1]
    part_1 = max(calculate_seat_id(seat) for seat in seats)
    print(f"Part 1: {part_1}")

    all_seat_ids = set(range(7112 + 1))
    present_seat_ids = {calculate_seat_id(seat) for seat in seats}
    missing_seat_ids = all_seat_ids - present_seat_ids

    my_seat_id = [
        seat_id for seat_id in missing_seat_ids
        if seat_id - 1 in present_seat_ids and seat_id + 1 in present_seat_ids
    ][0]
    print(f"Part 2: {my_seat_id}")
