#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')



#
# Complete the 'extractAndAppendSponsoredNodes' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST head as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#

    
def extractAndAppendSponsoredNodes(head):
    if not head or not head.next:
        return head

    odd_head = odd_tail = None
    even_reversed = None

    index = 0
    curr = head

    while curr:
        next_node = curr.next
        curr.next = None

        if index % 2 == 0:
            curr.next = even_reversed
            even_reversed = curr
        else:
            if not odd_head:
                odd_head = odd_tail = curr
            else:
                odd_tail.next = curr
                odd_tail = curr

        curr = next_node
        index += 1

    if odd_tail:
        odd_tail.next = even_reversed
        return odd_head
    else:
        return even_reversed

if __name__ == '__main__':
    head_count = int(input().strip())

    head = SinglyLinkedList()

    for _ in range(head_count):
        head_item = int(input().strip())
        head.insert_node(head_item)

    result = extractAndAppendSponsoredNodes(head.head)

    print_singly_linked_list(result, '\n')
    print()
