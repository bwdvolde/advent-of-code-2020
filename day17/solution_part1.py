from read_file.read_file import read_file


class Cell:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return str(tuple(self))

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        return hash(tuple(self))

def neighbours(cell):
    result = {Cell(x, y, z) for x in [cell.x - 1, cell.x, cell.x + 1] for y in [cell.y - 1, cell.y, cell.y + 1] for z in
          [cell.z - 1, cell.z, cell.z + 1] if (x, y, z) != (cell.x, cell.y, cell.z)}
    return result

def print_cells(cells):
    min_x = min(cell.x for cell in cells)
    max_x = max(cell.x for cell in cells)
    min_y = min(cell.y for cell in cells)
    max_y = max(cell.y for cell in cells)
    min_z = min(cell.z for cell in cells)
    max_z = max(cell.z for cell in cells)
    for z in range(min_z, max_z + 1):
        print(f'z={z}')
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if Cell(x, y, z) in cells:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
        print()

ACTIVE = "#"
if __name__ == '__main__':
    lines = read_file("input.txt")

    active_cells = {Cell(x, y, 0) for y, line in enumerate(lines) for x, char in enumerate(line)
                    if line and char == ACTIVE}

    def active_neighbours(cell):
        return len([neighbour for neighbour in neighbours(cell) if neighbour in active_cells])

    cycles = 6
    for cycle in range(cycles):
        to_remove = set()
        to_add = set()

        to_check = active_cells | {neighbour for cell in active_cells for neighbour in neighbours(cell)}

        to_add |= {cell for cell in to_check if cell not in active_cells and active_neighbours(cell) == 3}
        to_remove |= {cell for cell in to_check if cell in active_cells and active_neighbours(cell) not in [2, 3]}

        assert not to_add & to_remove
        active_cells = (active_cells - to_remove) | to_add

    print(f"Part 1: {len(active_cells)}")


