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

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):


    op_node = head
    next_1_node = op_node.next
    next_2_node = next_1_node.next

    while next_1_node is not None:

        # reverse direction of next_1_node
        next_1_node.next = op_node

        if op_node == head:
            # corner case handling
            op_node.next = None

        # op node move forward
        op_node = next_1_node

        # next 1 node move forward
        next_1_node = next_2_node

        if next_2_node is not None:
            next_2_node = next_2_node.next

        else:
            # mark the tail node as the head of reversed linked list
            head = op_node
    
    # return the head of reversed linked list
    return head



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
