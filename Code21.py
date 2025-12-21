#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxDistinctSubstringLengthInSessions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING sessionString as parameter.
#

def maxDistinctSubstringLengthInSessions(sessionString):
    if not sessionString or set(sessionString) == {"*"} :
        return 0
    seen=set()# Write your code here
    left=0
    longest=0
    for i in range(len(sessionString)):
        if sessionString[i] == '*':
            seen.clear()
            left = i + 1
            continue

        while sessionString[i] in seen:
            seen.remove(sessionString[left])
            left+=1
        seen.add(sessionString[i])
        longest=max(longest,i-left+1)
    return longest
        

if __name__ == '__main__':
    sessionString = input()

    result = maxDistinctSubstringLengthInSessions(sessionString)

    print(result)
