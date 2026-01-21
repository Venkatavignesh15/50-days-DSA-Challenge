#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    start = 0
    balance = 0
    deficit = 0

    for i in range(len(petrolpumps)):
        petrol = petrolpumps[i][0]
        distance = petrolpumps[i][1]

        balance += petrol - distance

        if balance < 0:
            deficit += balance
            start = i + 1
            balance = 0

    if balance + deficit >= 0:
        return start
    else:
        return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
