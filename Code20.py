#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'canPlaceSecurityCameras' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER N
#  2. 2D_INTEGER_ARRAY grid
#

def canPlaceSecurityCameras(N, grid):
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col

    def backtrack(row):
        if row == N:
            return True

        for col in range(N):
            if grid[row][col] == 0 and col not in cols \
               and (row - col) not in diag1 \
               and (row + col) not in diag2:

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                if backtrack(row + 1):
                    return True

                # backtrack
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        return False

    return backtrack(0)

if __name__ == '__main__':
    N = int(input().strip())

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = canPlaceSecurityCameras(N, grid)

    print(int(result))
