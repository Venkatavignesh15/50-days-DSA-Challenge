#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'processRequestQueueOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY operations
#  2. INTEGER_ARRAY values
#
def processRequestQueueOperations(operations, values):
    instack=[]
    outstack=[]
    result=[]
    for i in range(len(operations)):
        if operations[i]=="enqueue":
            instack.append(values[i])
            
        elif operations[i]=="dequeue":
            if outstack:
                result.append(outstack.pop())
            elif not outstack:
                while instack:
                    outstack.append(instack.pop())
                result.append(outstack.pop())
                    
        elif operations[i]=="size":
            siz=len(instack)+len(outstack)
            result.append(siz)
            
        elif operations[i]=="peek":
            if not outstack:
                while instack:
                    outstack.append(instack.pop())
                result.append(outstack[-1])
            elif outstack:
                result.append(outstack[-1])
    return result
                    
                
    

if __name__ == '__main__':
    operations_count = int(input().strip())

    operations = []

    for _ in range(operations_count):
        operations_item = input()
        operations.append(operations_item)

    values_count = int(input().strip())

    values = []

    for _ in range(values_count):
        values_item = int(input().strip())
        values.append(values_item)

    result = processRequestQueueOperations(operations, values)

    print('\n'.join(map(str, result)))
