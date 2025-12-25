#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findPeakIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY counts as parameter.
#

def findPeakIndex(counts):
    low=0
    high=len(counts)-1
    while low<high:
        mid=(low+high)//2
        if counts[mid] >counts[mid+1]:
            high=mid
        else:
            low=mid+1
        if low==high:
            break
    return high 

if __name__ == '__main__':
    counts_count = int(input().strip())

    counts = []

    for _ in range(counts_count):
        counts_item = int(input().strip())
        counts.append(counts_item)

    result = findPeakIndex(counts)

    print(result)
