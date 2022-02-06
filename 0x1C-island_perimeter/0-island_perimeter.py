#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculates the perimeter of an island
    """
    # Initialize perimeter
    perimeter = 0
    # Iterate through the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Check if the cell is a land
            if grid[i][j] == 1:
                # Check if the cell is on the left edge
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check if the cell is on the right edge
                if j == len(grid[i])-1 or grid[i][j+1] == 0:
                    perimeter += 1
                # Check if the cell is on the top edge
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check if the cell is on the bottom edge
                if i == len(grid)-1 or grid[i+1][j] == 0:
                    perimeter += 1

    return perimeter