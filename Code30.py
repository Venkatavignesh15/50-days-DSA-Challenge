#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'allocateBandwidthMaxRevenue' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER_ARRAY sizes
#  3. INTEGER_ARRAY revenues
#  4. LONG_INTEGER B
#

def allocateBandwidthMaxRevenue(N, sizes, revenues, B):
    # Write your code here
    if B==0 and not sizes:
        return 0.0
    stream=[]
    result=0
    for i in range(N):
        stream.append((revenues[i]/sizes[i],revenues[i],sizes[i]))
    
    stream.sort(reverse=True, key=lambda x: x[0])
    
    for density,revenue,size in stream:
        if B>=size:
            result+=revenue
            B-=size
        else:
            result+=revenue*(B/size)
            break
    return (float(result))
        
            
        
        

if __name__ == '__main__':
    N = int(input().strip())

    sizes_count = int(input().strip())

    sizes = []

    for _ in range(sizes_count):
        sizes_item = int(input().strip())
        sizes.append(sizes_item)

    revenues_count = int(input().strip())

    revenues = []

    for _ in range(revenues_count):
        revenues_item = int(input().strip())
        revenues.append(revenues_item)

    B = int(input().strip())

    result = allocateBandwidthMaxRevenue(N, sizes, revenues, B)

    print(result)
