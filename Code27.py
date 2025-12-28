#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTopKFrequentEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY events
#  2. INTEGER k
#

def getTopKFrequentEvents(events, k):
    freq = {}
    first_index = {}

    for i, e in enumerate(events):
        if e not in freq:
            freq[e] = 0
            first_index[e] = i
        freq[e] += 1

    sorted_events = sorted(
        freq.keys(),
        key=lambda x: (-freq[x], first_index[x])
    )

    return sorted_events[:k]
    
    

if __name__ == '__main__':
    events_count = int(input().strip())

    events = []

    for _ in range(events_count):
        events_item = int(input().strip())
        events.append(events_item)

    k = int(input().strip())

    result = getTopKFrequentEvents(events, k)

    print('\n'.join(map(str, result)))
