from read_file.read_file import read_file


def calculate_starting_black_tiles():
    lines = read_file("input.txt")
    lines = [line for line in lines if line]
    black_tiles = set()

    for line in lines:
        position = (0, 0)
        i = 0
        while i < len(line):
            row, col = position
            if line[i] == "e":
                position = (row + 0, col + 2)
                i += 1
            elif line[i] == "w":
                position = (row + 0, col - 2)
                i += 1
            elif line[i:i + 2] == "se":
                position = (row + 1, col + 1)
                i += 2
            elif line[i:i + 2] == "sw":
                position = (row + 1, col - 1)
                i += 2
            elif line[i:i + 2] == "nw":
                position = (row - 1, col - 1)
                i += 2
            elif line[i:i + 2] == "ne":
                position = (row - 1, col + 1)
                i += 2

        if position in black_tiles:
            black_tiles.remove(position)
        else:
            black_tiles.add(position)

    return black_tiles


def neighbours(position):
    row, col = position
    return {
        (row, col + 2),
        (row, col - 2),
        (row - 1, col - 1),
        (row - 1, col + 1),
        (row + 1, col - 1),
        (row + 1, col + 1),
    }


if __name__ == '__main__':
    black_tiles = calculate_starting_black_tiles()
    print(f"Part 1: {len(black_tiles)}")

    def black_neighbours(position):
        return len(black_tiles & neighbours(position))

    cycles = 100
    for cycle in range(cycles):
        to_remove = set()
        to_add = set()

        to_check = black_tiles | {neighbour for tile in black_tiles for neighbour in neighbours(tile)}

        to_add |= {cell for cell in to_check if cell not in black_tiles and black_neighbours(cell) == 2}
        to_remove |= {cell for cell in to_check if cell in black_tiles and black_neighbours(cell) == 0 or black_neighbours(cell) > 2}

        assert not to_add & to_remove
        black_tiles = (black_tiles - to_remove) | to_add

    print(f"Part 2: {len(black_tiles)}")

