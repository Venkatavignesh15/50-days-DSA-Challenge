#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'processCouponStackOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def processCouponStackOperations(operations):
    class Stack:
        def __init__(self):
            self.stack = []
            self.min_stack = []  

        def push(self, x):
            x = int(x)
            self.stack.append(x)
            if not self.min_stack or x <= self.min_stack[-1]:
                self.min_stack.append(x)

        def pop(self):
            removed = self.stack.pop()
            if removed == self.min_stack[-1]:
                self.min_stack.pop()

        def top(self):
            return self.stack[-1]

        def getMin(self):
            return self.min_stack[-1]

    s = Stack()
    result = []

    for op in operations:
        parts = op.split()
        command = parts[0]

        if command == "push":
            s.push(parts[1])

        elif command == "pop":
            s.pop()

        elif command == "top":
            result.append(s.top())

        elif command == "getMin":
            result.append(s.getMin())

    return result

            

if __name__ == '__main__':
    operations_count = int(input().strip())

    operations = []

    for _ in range(operations_count):
        operations_item = input()
        operations.append(operations_item)

    result = processCouponStackOperations(operations)

    print('\n'.join(map(str, result)))
