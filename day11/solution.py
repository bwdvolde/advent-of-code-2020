from copy import deepcopy

from read_file.read_file import read_file

FLOOR = "."
EMPTY_SEAT = "L"
OCCUPIED_SEAT = "#"


def out_of_bounds(grid, r, c):
    return r < 0 or r >= len(
        grid) or c < 0 or c >= len(grid[0])


def neighbors_part_1(grid, r, c):
    count = 0
    for neighbor_r in [r - 1, r, r + 1]:
        for neighbor_c in [c - 1, c, c + 1]:
            if (neighbor_r == r and neighbor_c == c) or out_of_bounds(grid, neighbor_r, neighbor_c):
                continue
            count += grid[neighbor_r][neighbor_c] == OCCUPIED_SEAT

    return count


def neighbors_part_2(grid, r, c):
    count = 0

    diffs = [
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0),
        (1, -1),
        (1, 1),
        (-1, -1),
        (-1, 1)
    ]

    for dr, dy in diffs:
        current_r, current_c = r + dr, c + dy
        while not out_of_bounds(grid, current_r, current_c) and grid[current_r][current_c] == FLOOR:
            current_r, current_c = current_r + dr, current_c + dy
        if not out_of_bounds(grid, current_r, current_c) and grid[current_r][current_c] == OCCUPIED_SEAT:
            count += 1

    return count


def find_stable_occupied_seats(grid, calculation_method, min_neighbors):
    current_grid = deepcopy(grid)
    changed = True
    while changed:
        changed = False
        new_grid = deepcopy(current_grid)

        for r in range(len(current_grid)):
            for c in range(len(current_grid[r])):
                seat = current_grid[r][c]
                n_neighbors = calculation_method(current_grid, r, c)
                if seat == EMPTY_SEAT and n_neighbors == 0:
                    new_grid[r][c] = OCCUPIED_SEAT
                    changed = True
                if seat == OCCUPIED_SEAT and n_neighbors >= min_neighbors:
                    new_grid[r][c] = EMPTY_SEAT
                    changed = True

        current_grid = new_grid
    return sum(seat == OCCUPIED_SEAT for row in current_grid for seat in row)


if __name__ == '__main__':
    lines = read_file("input.txt")
    grid = [[place for place in row] for row in lines if row]

    answer_part_1 = find_stable_occupied_seats(grid, neighbors_part_1, 4)
    print(f"Part 1: {answer_part_1}")

    answer_part_2 = find_stable_occupied_seats(grid, neighbors_part_2, 5)
    print(f"Part 2: {answer_part_2}")
