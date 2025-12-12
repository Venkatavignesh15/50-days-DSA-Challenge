#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'debounceTimestamps' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY timestamps
#  2. INTEGER K
#

def debounceTimestamps(timestamps, K):
    n=len(timestamps)
    t=timestamps
    if n == 0:
        return 0
    f = t[0]
    res=[]
    res.append(f) #  Write your code here
    for i in range(1,n):
        if (t[i] - f) >= K:
            f=t[i]
            res.append(f)
    return len(res)
            

if __name__ == '__main__':
    timestamps_count = int(input().strip())

    timestamps = []

    for _ in range(timestamps_count):
        timestamps_item = int(input().strip())
        timestamps.append(timestamps_item)

    K = int(input().strip())

    result = debounceTimestamps(timestamps, K)

    print(result)
