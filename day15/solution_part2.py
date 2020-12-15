import heapq

if __name__ == '__main__':
    starting_numbers = [1,12,0,20,8,16]

    last_spoken_of = {}

    for i, starting_number in enumerate(starting_numbers[:-1]):
        last_spoken_of[starting_number] = i + 1

    print(last_spoken_of)

    previous_spoken = starting_numbers[-1]
    n_turns = 30000000
    for turn in range(len(starting_numbers) + 1, n_turns + 1):
        if not turn % 100000:
            print(turn)
        if previous_spoken not in last_spoken_of:
            new_number_spoken = 0
        else:
            new_number_spoken = (turn - 1) - last_spoken_of[previous_spoken]

        last_spoken_of[previous_spoken] = turn - 1
        previous_spoken = new_number_spoken

    print(f"Part 2: {previous_spoken}")




