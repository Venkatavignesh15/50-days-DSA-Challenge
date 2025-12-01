#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
#

def isAlphabeticPalindrome(code):
    word=''
    for i in code:
        if i.isalpha():
                word+=i
    words=word.lower()
    return words==words[::-1]
        # Write your code here

if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
