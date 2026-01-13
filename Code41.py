#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSmallestSubstringWindow' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY patterns
#  2. STRING S
#

def findSmallestSubstringWindow(patterns, S):
    occurrences = []

    # Step 1: find all pattern matches
    for pid, pat in enumerate(patterns):
        start = S.find(pat)
        while start != -1:
            occurrences.append((start, start + len(pat) - 1, pid))
            start = S.find(pat, start + 1)

    if not occurrences:
        return [-1, -1]

    # Step 2: sort by starting index
    occurrences.sort()

    from collections import defaultdict
    count = defaultdict(int)

    required = len(patterns)
    formed = 0

    left = 0
    ans = (-1, -1, float('inf'))

    # Sliding Window
    for right in range(len(occurrences)):
        s, e, pid = occurrences[right]

        if count[pid] == 0:
            formed += 1
        count[pid] += 1

        while formed == required:
            s2, e2, pid2 = occurrences[left]

            if e - s2 < ans[2]:
                ans = (s2, e, e - s2)

            count[pid2] -= 1
            if count[pid2] == 0:
                formed -= 1

            left += 1

    if ans[0] == -1:
        return [-1, -1]

    return [ans[0], ans[1]]


if __name__ == '__main__':
    patterns_count = int(input().strip())

    patterns = []

    for _ in range(patterns_count):
        patterns_item = input()
        patterns.append(patterns_item)

    S = input()

    result = findSmallestSubstringWindow(patterns, S)

    print('\n'.join(map(str, result)))
