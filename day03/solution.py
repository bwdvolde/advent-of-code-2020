from read_file.read_file import read_file


def calculate_trees(grid, slope_row, slope_col):
    r = 0
    c = 0
    count = 0
    while r < len(grid):
        if grid[r][c] == "#":
            count += 1

        r += slope_row
        c = (c + slope_col) % len(grid[0])

    return count


if __name__ == '__main__':
    lines = read_file("input.txt")
    grid = [[c for c in line] for line in lines if line]

    part_1 = calculate_trees(grid, 1, 3)
    print(f"Part 1: {part_1}")

    slope_pairs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    part_2 = 1
    for slope_col, slope_row in slope_pairs:
        trees = calculate_trees(grid, slope_row, slope_col)
        part_2 *= trees

    print(f"Part 2: {part_2}")


