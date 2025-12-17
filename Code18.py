#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countIsolatedCommunicationGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY links
#  2. INTEGER n
#
from collections import  deque
def countIsolatedCommunicationGroups(links, n):
    graph = {i: [] for i in range(n)}
    for a, b in links:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            count += 1
            q = deque([i])
            visited[i] = True
            while q:
                curr = q.popleft()
                for nei in graph[curr]:
                    if not visited[nei]:
                        visited[nei] = True
                        q.append(nei)

    return count

                
    

if __name__ == '__main__':
    links_rows = int(input().strip())
    links_columns = int(input().strip())

    links = []

    for _ in range(links_rows):
        links.append(list(map(int, input().rstrip().split())))

    n = int(input().strip())

    result = countIsolatedCommunicationGroups(links, n)

    print(result)
