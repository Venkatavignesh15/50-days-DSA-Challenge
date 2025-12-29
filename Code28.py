#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'searchRotatedTimestamps' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def searchRotatedTimestamps(nums, target):
    if not nums:
        return -1
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
    pivot = low

    # Decide search space
    if nums[pivot] <= target <= nums[-1]:
        low, high = pivot, len(nums) - 1
    else:
        low, high = 0, pivot - 1

    # Binary search
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
        
        

if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    target = int(input().strip())

    result = searchRotatedTimestamps(nums, target)

    print(result)
