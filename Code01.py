#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    if not responseTimes:
        return 0
    lst=[responseTimes[0]]
    count=0
    if len(responseTimes)<=1:
        return count
    for i in range(1,len(responseTimes)):
        pre_avg=sum(lst)/len(lst)
        if responseTimes[i]>pre_avg:
                count+=1
        lst.append(responseTimes[i])
    return count

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
