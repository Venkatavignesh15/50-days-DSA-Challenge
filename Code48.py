#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'completeDiagonalSudokuGrid' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def completeDiagonalSudokuGrid(grid):
    # Write your code here
    def is_valid(r, c, num):
        # Row check
        for x in range(9):
            if grid[r][x] == num:
                return False

        # Column check
        for x in range(9):
            if grid[x][c] == num:
                return False

        # 3x3 block check
        br, bc = (r // 3) * 3, (c // 3) * 3
        for i in range(br, br + 3):
            for j in range(bc, bc + 3):
                if grid[i][j] == num:
                    return False

        # Main diagonal
        if r == c:
            for i in range(9):
                if grid[i][i] == num:
                    return False

        # Anti-diagonal
        if r + c == 8:
            for i in range(9):
                if grid[i][8 - i] == num:
                    return False

        return True

    def backtrack():
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    for num in range(1, 10):
                        if is_valid(i, j, num):
                            grid[i][j] = num
                            if backtrack():
                                return True
                            grid[i][j] = 0
                    return False
        return True

    backtrack()
    return grid

if __name__ == '__main__':
    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = completeDiagonalSudokuGrid(grid)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
