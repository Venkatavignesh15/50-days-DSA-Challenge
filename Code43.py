#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

def twoStacks(maxSum, a, b):
    # Write your code here
    total = 0
    countA = 0

    while countA < len(a) and total + a[countA] <= maxSum:
        total += a[countA]
        countA += 1

    maxCount = countA
    countB = 0

    while countB < len(b):
        total += b[countB]
        countB += 1

        while total > maxSum and countA > 0:
            countA -= 1
            total -= a[countA]

        if total <= maxSum:
            maxCount = max(maxCount, countA + countB)

    return maxCount
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
