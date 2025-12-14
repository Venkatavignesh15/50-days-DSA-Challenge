#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minTasksToCancelForNoConflict' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING digits as parameter.
#

def minTasksToCancelForNoConflict(digits):
    def letterCombinations(digits):
        if not digits:
          return []

    mapping = {
        '0': '0',
        '1': '1',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    result = []

    def backtrack(index, path):
        if index == len(digits):
            result.append(path)
            return

        for ch in mapping[digits[index]]:
            backtrack(index + 1, path + ch)

    backtrack(0, "")
    return result

if __name__ == '__main__':
    digits = input()

    result = minTasksToCancelForNoConflict(digits)

    print('\n'.join(result))
