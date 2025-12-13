#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#

def isAnagram(s, t):
    if len(s)==len(t):
        if sorted(s)==sorted(t):
            return 1
        else:
            return 0
    return 0

if __name__ == '__main__':
    s = input()

    t = input()

    result = isAnagram(s, t)

    print(result)
