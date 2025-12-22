#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countSubarraysWithSumAndMaxAtMost' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. LONG_INTEGER k
#  3. LONG_INTEGER M
#
from collections import defaultdict
def countSubarraysWithSumAndMaxAtMost(nums, k, M):
    count = 0
    prefix_sum = 0
    freq = defaultdict(int)
    freq[0] = 1

    for num in nums:
        # Break the session if max constraint violated
        if num > M:
            prefix_sum = 0
            freq.clear()
            freq[0] = 1
            continue

        prefix_sum += num
        count += freq[prefix_sum - k]
        freq[prefix_sum] += 1

    return count

if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    k = int(input().strip())

    M = int(input().strip())

    result = countSubarraysWithSumAndMaxAtMost(nums, k, M)

    print(result)
