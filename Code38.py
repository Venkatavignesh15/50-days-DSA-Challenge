#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'hasCircularDependency' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY dependencies
#

def hasCircularDependency(n, dependencies):
    # Write your code here
    my_dict = {}
    for dep in dependencies:
        if dep[0] >=n or dep[1] >=n:
            continue
        if dep[0] == dep[1]:
            return 1
        if dep[0] not in my_dict:
            my_dict[dep[0]] = dep[1]
            
        start = dep[0]
        curr = dep[0]
        while curr in my_dict.keys():
            nex = my_dict[curr]
            if nex >= n:
                break
            if nex == start:
                return 1
            curr = nex
        
    return 0

if __name__ == '__main__':
    n = int(input().strip())

    dependencies_rows = int(input().strip())
    dependencies_columns = int(input().strip())

    dependencies = []

    for _ in range(dependencies_rows):
        dependencies.append(list(map(int, input().rstrip().split())))

    result = hasCircularDependency(n, dependencies)

    print(int(result))
