#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mergeHighDefinitionIntervals' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#
def mergeHighDefinitionIntervals(intervals):
    # Write your code here
    if not intervals:
        return []
    intervals.sort()
    merged=[]
    current=intervals[0]
    for i in range(1,len(intervals)):
        if current[1] >= intervals[i][0]:
            current[1]=max(current[1],intervals[i][1])
        else:
            merged.append(current)
            current=intervals[i]
    merged.append(current)
    return merged
                        
        

if __name__ == '__main__':
    intervals_rows = int(input().strip())
    intervals_columns = int(input().strip())

    intervals = []

    for _ in range(intervals_rows):
        intervals.append(list(map(int, input().rstrip().split())))

    result = mergeHighDefinitionIntervals(intervals)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
