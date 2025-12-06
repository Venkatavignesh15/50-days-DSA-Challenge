#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'areBracketsProperlyMatched' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code_snippet as parameter.
#

def areBracketsProperlyMatched(code_snippet):
    # Write your code here
    stack=[]
    par={')':'(','}':'{',']':'['}
    for i in code_snippet:
        if i in '({[':
            stack.append(i)
        elif i in ')]}':
            if not stack or stack[-1] != par[i]:
                return False
            stack.pop()
    return len(stack)==0

if __name__ == '__main__':
    code_snippet = input()

    result = areBracketsProperlyMatched(code_snippet)

    print(int(result))
