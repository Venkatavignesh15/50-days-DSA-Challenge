#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getAutoSaveInterval' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER n as parameter.
#

def getAutoSaveInterval(n):
    lst=[1,2]
    while n >= len(lst):
        for i in range(n-1):
            next_lst=lst[i]+lst[i+1]
            lst.append(next_lst)
    return (lst[n])

if __name__ == '__main__':
    n = int(input().strip())

    result = getAutoSaveInterval(n)

    print(result)
