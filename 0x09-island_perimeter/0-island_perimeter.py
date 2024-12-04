#!/usr/bin/python3
"""
a function def that returns the perimeter of
the island described in grid
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.
    :param grid: List of lists representing the grid (0 for water,
    1 for land)
    :return: Integer representing the perimeter of the island
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
