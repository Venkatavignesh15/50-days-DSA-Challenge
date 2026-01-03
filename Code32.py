#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findLongestArithmeticProgression' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER k
#

def findLongestArithmeticProgression(arr, k):
    if not arr:
        return 0
    # Write your code here
    lst=set(arr)
    max_n=0
    
    for i in lst:
        if i-k not in lst:
            current=i
            length=1
            while current+k in lst:
                current+=k
                length+=1
            max_n=max(max_n,length)
    return (max_n)
        
        
        

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    result = findLongestArithmeticProgression(arr, k)

    print(result)
