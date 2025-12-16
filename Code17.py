#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countInstallationSequences' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def countInstallationSequences(n):
    if n <= 1:
        return 1

    p2 = 1 
    p1 = 1 

    for _ in range(2, n + 1):
        curr = p1 + p2
        p2 = p1
        p1 = curr

    return p1


if __name__ == '__main__':
    n = int(input().strip())

    result = countInstallationSequences(n)

    print(result)
