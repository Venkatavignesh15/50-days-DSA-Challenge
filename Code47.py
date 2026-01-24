#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minTransformationCost' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY A
#  2. STRING_ARRAY B
#  3. INTEGER insertCost
#  4. INTEGER deleteCost
#

def minTransformationCost(A, B, insertCost, deleteCost):
    # Write your code here
    def edit_distance(s1, s2):
        n, m = len(s1), len(s2)
        if n == 0:
            return m
        if m == 0:
            return n

        prev = list(range(m + 1))
        curr = [0] * (m + 1)

        for i in range(1, n + 1):
            curr[0] = i
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = 1 + min(
                        prev[j],      # delete
                        curr[j - 1],  # insert
                        prev[j - 1]   # replace
                    )
            prev, curr = curr, prev

        return prev[m]

    n, m = len(A), len(B)

    # ---------- Line-level DP (space optimized) ----------
    prev = [j * insertCost for j in range(m + 1)]
    curr = [0] * (m + 1)

    for i in range(1, n + 1):
        curr[0] = i * deleteCost
        for j in range(1, m + 1):
            delete = prev[j] + deleteCost
            insert = curr[j - 1] + insertCost
            modify = prev[j - 1] + edit_distance(A[i - 1], B[j - 1])
            curr[j] = min(delete, insert, modify)
        prev, curr = curr, prev

    return prev[m]

if __name__ == '__main__':
    A_count = int(input().strip())

    A = []

    for _ in range(A_count):
        A_item = input()
        A.append(A_item)

    B_count = int(input().strip())

    B = []

    for _ in range(B_count):
        B_item = input()
        B.append(B_item)

    insertCost = int(input().strip())

    deleteCost = int(input().strip())

    result = minTransformationCost(A, B, insertCost, deleteCost)

    print(result)
