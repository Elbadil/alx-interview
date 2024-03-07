#!/usr/bin/python3
"""Defining a function called island_perimeter"""


def island_perimeter(grid):
    """Returns the perimeter of an island inside a grid"""
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if j + 1 >= len(grid[i]) or (j + 1 < len(grid[i])
                                             and grid[i][j + 1] != 1):
                    perimeter += 1
                if j - 1 < 0 or (j - 1 >= 0
                                 and grid[i][j - 1] != 1):
                    perimeter += 1
                if i - 1 < 0 or (i - 1 >= 0
                                 and grid[i - 1][j] != 1):
                    perimeter += 1
                if i + 1 >= len(grid) or (i + 1 < len(grid)
                                          and grid[i + 1][j] != 1):
                    perimeter += 1

    return perimeter
