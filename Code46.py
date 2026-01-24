#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'simulatePriorityCache' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER capacity
#  2. INTEGER numOperations
#  3. STRING_ARRAY operationTypes
#  4. INTEGER_ARRAY keys
#  5. INTEGER_ARRAY values
#  6. INTEGER_ARRAY priorities
#

def simulatePriorityCache(capacity, numOperations, operationTypes, keys, values, priorities):
    # Write your code here
    from collections import defaultdict

    # ---------- Node ----------
    class Node:
        def __init__(self, key, value, priority):
            self.key = key
            self.value = value
            self.priority = priority
            self.prev = None
            self.next = None

    # ---------- Doubly Linked List ----------
    class DoublyLinkedList:
        def __init__(self):
            self.head = Node(0, 0, 0)
            self.tail = Node(0, 0, 0)
            self.head.next = self.tail
            self.tail.prev = self.head
            self.size = 0

        def add_front(self, node):
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
            self.size += 1

        def remove(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1

        def remove_lru(self):
            if self.size == 0:
                return None
            node = self.tail.prev
            self.remove(node)
            return node

        def is_empty(self):
            return self.size == 0

    # ---------- Cache ----------
    key_map = {}                      # key -> node
    priority_map = defaultdict(DoublyLinkedList)
    min_priority = float('inf')
    size = 0
    result = []

    for i in range(numOperations):
        op = operationTypes[i]
        key = keys[i]

        # ---------- GET ----------
        if op == "get":
            if key not in key_map:
                result.append(-1)
            else:
                node = key_map[key]
                dll = priority_map[node.priority]
                dll.remove(node)
                dll.add_front(node)
                result.append(node.value)

        # ---------- PUT ----------
        elif op == "put":
            value = values[i]
            priority = priorities[i]

            if capacity == 0:
                continue

            if key in key_map:
                node = key_map[key]
                node.value = value
                if node.priority != priority:
                    # update priority
                    old_p = node.priority
                    priority_map[old_p].remove(node)
                    if priority_map[old_p].is_empty():
                        del priority_map[old_p]
                        if min_priority == old_p:
                            min_priority = min(priority_map.keys(), default=float('inf'))

                    node.priority = priority
                    priority_map[priority].add_front(node)
                    min_priority = min(min_priority, priority)
                else:
                    dll = priority_map[node.priority]
                    dll.remove(node)
                    dll.add_front(node)
            else:
                if size == capacity:
                    dll = priority_map[min_priority]
                    evicted = dll.remove_lru()
                    del key_map[evicted.key]
                    size -= 1
                    if dll.is_empty():
                        del priority_map[min_priority]

                node = Node(key, value, priority)
                key_map[key] = node
                priority_map[priority].add_front(node)
                min_priority = min(min_priority, priority)
                size += 1

        # ---------- UPDATE PRIORITY ----------
        else:  # updatePriority
            new_priority = priorities[i]
            if key in key_map:
                node = key_map[key]
                old_p = node.priority
                priority_map[old_p].remove(node)
                if priority_map[old_p].is_empty():
                    del priority_map[old_p]
                    if min_priority == old_p:
                        min_priority = min(priority_map.keys(), default=float('inf'))

                node.priority = new_priority
                priority_map[new_priority].add_front(node)
                min_priority = min(min_priority, new_priority)

    return result
    

if __name__ == '__main__':
    capacity = int(input().strip())

    numOperations = int(input().strip())

    operationTypes_count = int(input().strip())

    operationTypes = []

    for _ in range(operationTypes_count):
        operationTypes_item = input()
        operationTypes.append(operationTypes_item)

    keys_count = int(input().strip())

    keys = []

    for _ in range(keys_count):
        keys_item = int(input().strip())
        keys.append(keys_item)

    values_count = int(input().strip())

    values = []

    for _ in range(values_count):
        values_item = int(input().strip())
        values.append(values_item)

    priorities_count = int(input().strip())

    priorities = []

    for _ in range(priorities_count):
        priorities_item = int(input().strip())
        priorities.append(priorities_item)

    result = simulatePriorityCache(capacity, numOperations, operationTypes, keys, values, priorities)

    print('\n'.join(map(str, result)))
