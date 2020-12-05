from read_file.read_file import read_file


def calculate_seat_id(seat):
    return int(seat.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2)


if __name__ == '__main__':
    seats = read_file("input.txt")[:-1]
    part_1 = max(calculate_seat_id(seat) for seat in seats)
    print(f"Part 1: {part_1}")

    present_seat_ids = {calculate_seat_id(seat) for seat in seats}
    my_seat_id = [
        seat_id for seat_id in range(7112 + 1)
        if
        seat_id not in present_seat_ids
        and
        seat_id + 1 in present_seat_ids
        and seat_id - 1 in present_seat_ids
    ][0]
    print(f"Part 2: {my_seat_id}")
