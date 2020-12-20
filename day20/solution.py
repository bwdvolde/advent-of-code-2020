import re
from collections import Counter
import numpy as np
import math
import sys
from read_file.read_file import read_file

np.set_printoptions(linewidth=200)

sea_monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
sea_monster = np.array([list(row) for row in sea_monster.split("\n")])
sea_monster_rows = len(sea_monster)
sea_monster_cols = len(sea_monster[0])


class Tile:

    def __init__(self, tile_id, grid):
        self.tile_id = tile_id
        self.grid = grid
        self.top_hash = hash(tuple(grid[0]))
        self.bottom_hash = hash(tuple(grid[-1]))
        self.left_hash = hash(tuple(grid[:, 0]))
        self.right_hash = hash(tuple(grid[:, -1]))
        self.border_hashes = {self.top_hash, self.bottom_hash, self.left_hash, self.right_hash}


def find_corner_ids(tiles):
    counts = Counter(border_hash for tile in tiles for border_hash in tile.border_hashes)
    image_border_hashes = {border_hash for border_hash, count in counts.items() if count == 8}
    corner_ids = set()
    for tile in tiles:
        a = len(tile.border_hashes & image_border_hashes)
        if a == 2:
            corner_ids.add(tile.tile_id)
    return corner_ids, image_border_hashes


if __name__ == '__main__':
    lines = read_file("input.txt")

    base_tiles = {}
    current_tile = []
    for line in lines:
        if not line:
            base_tiles[tile_id] = current_tile
            current_tile = []
        elif match := re.match("Tile ([0-9]+):", line):
            tile_id = int(match.group(1))
        else:
            row = list(line)
            current_tile.append(row)
    dimension = int(math.sqrt(len(base_tiles)))
    tiles = []
    for tile_id, base_tile in base_tiles.items():
        original = np.array(base_tile)
        vertical_flip = np.flipud(original)
        horizontal_flip = np.fliplr(original)
        horizontal_and_vertical_flip = np.fliplr(vertical_flip)

        for tile in [original, vertical_flip, horizontal_flip, horizontal_and_vertical_flip]:
            current = tile
            tiles.append(Tile(tile_id, current))
            for _ in range(3):
                current = np.rot90(current)
                tiles.append(Tile(tile_id, current))

    corner_ids, image_border_hashes = find_corner_ids(tiles)
    print(f"Part 1: {math.prod(corner_ids)}")

    current_tile = None
    iterator = iter(tiles)
    while (tile := next(iterator)) and not current_tile:
        if tile.top_hash in image_border_hashes and tile.left_hash in image_border_hashes:
            current_tile = tile

    remaining_tiles = [tile for tile in tiles if not tile.tile_id == current_tile.tile_id]
    image_tiles = [[None for _ in range(dimension)] for _ in range(dimension)]
    image_tiles[0][0] = current_tile
    for r in range(dimension):
        for c in range(dimension):
            if r == 0 and c == 0:
                continue
            elif c == 0:
                for tile in remaining_tiles:
                    if tile.top_hash == image_tiles[r - 1][c].bottom_hash:
                        image_tiles[r][c] = tile
                        remaining_tiles = [_tile for _tile in remaining_tiles if _tile.tile_id != tile.tile_id]
                        break
            else:
                for tile in remaining_tiles:
                    if tile.left_hash == image_tiles[r][c - 1].right_hash:
                        image_tiles[r][c] = tile
                        remaining_tiles = [_tile for _tile in remaining_tiles if _tile.tile_id != tile.tile_id]
                        break

    rows = [np.concatenate([image_tiles[r][c].grid[1:-1, 1:-1] for c in range(dimension)], axis=1) for r in
            range(dimension)]
    original = np.concatenate(rows, axis=0)
    vertical_flip = np.flipud(original)
    horizontal_flip = np.fliplr(original)
    horizontal_and_vertical_flip = np.fliplr(vertical_flip)

    for not_rotated_image in [original, vertical_flip, horizontal_flip, horizontal_and_vertical_flip]:
        for image in [not_rotated_image, np.rot90(not_rotated_image), np.rot90(np.rot90(not_rotated_image)),
                      np.rot90(np.rot90(np.rot90(not_rotated_image)))]:

            not_in_sea_monster = set()
            for r in range(len(image)):
                for c in range(len(image[r])):
                    if image[r, c] == "#":
                        not_in_sea_monster.add((r, c))
            original_not_in_sea_monster_length = len(not_in_sea_monster)

            for r in range(len(image) - sea_monster_rows + 1):
                for c in range(len(image[0]) - sea_monster_cols + 1):
                    sub_image = image[r:r + sea_monster_rows, c:c + sea_monster_cols]

                    is_match = True
                    in_sea_monster = set()
                    for sr in range(len(sub_image)):
                        for sc in range(len(sub_image[sr])):
                            if sea_monster[sr, sc] == '#' and sub_image[sr, sc] != "#":
                                is_match = False
                                break
                            elif sea_monster[sr, sc] == "#" and sub_image[sr, sc] == "#":
                                in_sea_monster.add((r + sr, c + sc))

                    if is_match:
                        not_in_sea_monster -= in_sea_monster

            if len(not_in_sea_monster) < original_not_in_sea_monster_length:
                print(f"Part 2: {len(not_in_sea_monster)}")
                sys.exit()
