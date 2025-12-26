#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findNextGreaterElementsWithDistance' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY readings as parameter.
#

def findNextGreaterElementsWithDistance(readings):
    res=[]
    for i in range(len(readings)):
        found= False
        for j in range(i+1,len(readings)):
            if readings[i]<readings[j]:
                res.append([readings[j],j-i])
                found= True
                break
        if not found:
            res.append([-1,-1])
    return res

if __name__ == '__main__':
    readings_count = int(input().strip())

    readings = []

    for _ in range(readings_count):
        readings_item = int(input().strip())
        readings.append(readings_item)

    result = findNextGreaterElementsWithDistance(readings)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
