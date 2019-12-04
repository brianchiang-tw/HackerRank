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

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):

    cur_1, cur_2 = head1, head2

    path_of_1, path_of_2 = set(), set()

    while True:

        path_of_1.add( cur_1 )
        path_of_2.add( cur_2 )

        merge = path_of_1.intersection( path_of_2 )
        if 0 != len(merge):
            return merge.pop().data

        next_of_cur_1 = cur_1.next
        next_of_cur_2 = cur_2.next

        if( next_of_cur_1 is not None):
            # cur_1 move forward
            cur_1 = next_of_cur_1

        if( next_of_cur_2 is not None):
            # cur_2 move forward
            cur_2 = next_of_cur_2

        
        

    return -1



if __name__ == '__main__':