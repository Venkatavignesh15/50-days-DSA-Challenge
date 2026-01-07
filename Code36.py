#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'computeLongestIncreasingSubsequenceLength' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY quality
#

def computeLongestIncreasingSubsequenceLength(n, quality):
    # Write your code here
    if n == 0:
        return 0
    tail=[quality[0]]
    for i in range(1,n):
        if tail[-1]<quality[i]:
            tail.extend([quality[i]])
        else:
            left, right = 0, len(tail) - 1
            while left <= right:
                mid = (left + right) // 2
                if tail[mid] >= quality[i]:
                    right = mid - 1
                else:
                    left = mid + 1
            tail[left] = quality[i]

    return len(tail)    

if __name__ == '__main__':
    n = int(input().strip())

    quality_count = int(input().strip())

    quality = []

    for _ in range(quality_count):
        quality_item = int(input().strip())
        quality.append(quality_item)

    result = computeLongestIncreasingSubsequenceLength(n, quality)

    print(result)
