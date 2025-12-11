#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'generateAngleBracketSequences' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER n as parameter.
#

def generateAngleBracketSequences(n):
    result = []

    def backtrack(s, open_used, close_used):
        if open_used == n and close_used == n:
            result.append(s)
            return
        if open_used < n:                    
            backtrack(s + "<", open_used + 1, close_used)
        if close_used < open_used:      
            backtrack(s + ">", open_used, close_used + 1)

    backtrack("", 0, 0)
    return result
            
     
if __name__ == '__main__':
    n = int(input().strip())

    result = generateAngleBracketSequences(n)

    print('\n'.join(result))
