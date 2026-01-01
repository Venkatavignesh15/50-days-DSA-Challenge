#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'computeShortestDeliveryTimes' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY handlingTimes
#  3. INTEGER m
#  4. 2D_INTEGER_ARRAY routes
#  5. INTEGER source
#
import heapq
def computeShortestDeliveryTimes(n, handlingTimes, m, routes, source):
    # Write your code here
    graph = [[] for _ in range(n)]
    for u, v, w in routes:
        graph[u].append((v, w))

    INF = float('inf')
    dist = [INF] * n
    dist[source] = 0

    pq = [(0, source)]

    while pq:
        curr_dist, u = heapq.heappop(pq)

        if curr_dist > dist[u]:
            continue

        for v, w in graph[u]:

            extra = handlingTimes[u] if u != source else 0
            new_dist = curr_dist + w + extra

            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    # Replace INF with -1
    return [-1 if d == INF else d for d in dist]

if __name__ == '__main__':
    n = int(input().strip())

    handlingTimes_count = int(input().strip())

    handlingTimes = []

    for _ in range(handlingTimes_count):
        handlingTimes_item = int(input().strip())
        handlingTimes.append(handlingTimes_item)

    m = int(input().strip())

    routes_rows = int(input().strip())
    routes_columns = int(input().strip())

    routes = []

    for _ in range(routes_rows):
        routes.append(list(map(int, input().rstrip().split())))

    source = int(input().strip())

    result = computeShortestDeliveryTimes(n, handlingTimes, m, routes, source)

    print('\n'.join(map(str, result)))
