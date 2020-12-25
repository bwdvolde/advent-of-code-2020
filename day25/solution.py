def calculate_loop_size(subject_number, goal):
    value = 1
    loop_size = 0
    while value != goal:
        loop_size += 1
        value *= subject_number
        value = value % 20201227

    return loop_size


def loop(subject_number, n_loops):
    value = 1
    for _ in range(n_loops):
        value *= subject_number
        value = value % 20201227

    return value


if __name__ == '__main__':
    card_public_key = 8458505
    door_public_key = 16050997
    # card_public_key = 5764801
    # door_public_key = 17807724

    card_loop_size = calculate_loop_size(7, card_public_key)
    door_loop_size = calculate_loop_size(7, door_public_key)
    print(card_loop_size, door_loop_size)
    print(f"Part 1: {loop(door_public_key, card_loop_size)}")
    print(f"Part 1: {loop(card_public_key, door_loop_size)}")
