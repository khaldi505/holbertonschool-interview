#!/usr/bin/python3

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    The island is
    described as a matrix of 0s and 1s.
    0 represents water
    """


    # Initialize perimeter
    perimeter = 0

    # Loop through the grid
    for row in range(len(grid)):
        for col in range(len(grid[row])):

            # If the cell is land, check the 4 adjacent cells
            if grid[
                row
            ][col] == 1:

                # Check the cell to the right
                if col + 1 < len(grid[row]) and grid[row][col + 1] == 1:
                    perimeter += 1

                # Check the cell to the left
                if col - 1 >= 0 and grid[row][col - 1] == 1:
                    perimeter += 1

                # Check the cell below
                if row + 1 < len(grid) and grid[row + 1][col] == 1:
                    perimeter += 1

                # Check the cell above
                if row - 1 >= 0 and grid[row - 1][col] == 1:
                    perimeter += 1

    return perimeter
