#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maximizeParallelTaskProfit' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER_ARRAY deadlines
#  4. INTEGER_ARRAY profits
#
import heapq
def maximizeParallelTaskProfit(n, m, deadlines, profits):
    tasks = list(zip(deadlines, profits))
    tasks.sort()
    
    min_heap = []
    
    for d, p in tasks:
        heapq.heappush(min_heap, p)
        
        if len(min_heap) > d * m:
            heapq.heappop(min_heap)
    
    return sum(min_heap)
    

if __name__ == '__main__':
    n = int(input().strip())

    m = int(input().strip())

    deadlines_count = int(input().strip())

    deadlines = []

    for _ in range(deadlines_count):
        deadlines_item = int(input().strip())
        deadlines.append(deadlines_item)

    profits_count = int(input().strip())

    profits = []

    for _ in range(profits_count):
        profits_item = int(input().strip())
        profits.append(profits_item)

    result = maximizeParallelTaskProfit(n, m, deadlines, profits)

    print(result)
