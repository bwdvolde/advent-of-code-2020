import re
from collections import Counter
from functools import lru_cache

import math

from read_file.read_file import read_file

if __name__ == '__main__':
    lines = read_file("input.txt")

    tiles = {}
    current_tile = []
    for line in lines:
        if not line:
            tiles[tile_id] = tuple(current_tile)
            current_tile = []
        elif match := re.match("Tile ([0-9]+):", line):
            tile_id = int(match.group(1))
        else:
            row = tuple(line)
            current_tile.append(row)


    @lru_cache
    def calculate_border_hashes(tile_id):
        tile = tiles[tile_id]
        top = tile[0]
        bottom = tile[-1]
        left = tuple(tile[r][0] for r in range(len(tile)))
        right = tuple(tile[r][-1] for r in range(len(tile)))

        top_reversed = tuple(reversed(top))
        bottom_reversed = tuple(reversed(bottom))
        left_reversed = tuple(reversed(left))
        right_reversed = tuple(reversed(right))

        return [
            hash(top),
            hash(bottom),
            hash(left),
            hash(right),
            hash(top_reversed),
            hash(bottom_reversed),
            hash(left_reversed),
            hash(right_reversed)
        ]

    def find_corner_tile_ids():
        counts = Counter(border_hash for tile_id in tiles.keys() for border_hash in calculate_border_hashes(tile_id))
        border_hashes_without_neighbour = {border_hash for border_hash, value in counts.items() if value == 1}

        corners = []
        for tile_id in tiles.keys():
            border_hashes = calculate_border_hashes(tile_id)
            borders_without_neighbour = sum(1 for border_hash in border_hashes if border_hash in border_hashes_without_neighbour)
            if borders_without_neighbour == 4:
                corners.append(tile_id)
        return corners


    corners = find_corner_tile_ids()
    print(f"Part 1: {math.prod(corners)}")

