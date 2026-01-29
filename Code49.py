#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'longestAlternatingSubstring' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def longestAlternatingSubstring(s, k):
    # Write your code here
    n = len(s)
    left = 0
    mismatch0 = 0  # mismatches for pattern starting with '0'
    mismatch1 = 0  # mismatches for pattern starting with '1'
    max_len = 0

    for right in range(n):
        # Expected characters at position right
        expected0 = '0' if right % 2 == 0 else '1'
        expected1 = '1' if right % 2 == 0 else '0'

        if s[right] != expected0:
            mismatch0 += 1
        if s[right] != expected1:
            mismatch1 += 1

        # Shrink window if both patterns exceed k flips
        while mismatch0 > k and mismatch1 > k:
            expected0_left = '0' if left % 2 == 0 else '1'
            expected1_left = '1' if left % 2 == 0 else '0'

            if s[left] != expected0_left:
                mismatch0 -= 1
            if s[left] != expected1_left:
                mismatch1 -= 1

            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == '__main__':
    s = input()

    k = int(input().strip())

    result = longestAlternatingSubstring(s, k)

    print(result)
