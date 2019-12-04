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

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):

    # dummy head node
    head_of_merge = SinglyLinkedListNode( 0 )
    merge_point = head_of_merge

    cur_1, cur_2 = head1, head2

    while( cur_1 is not None and cur_2 is not None):

        if cur_1.data <= cur_2.data:
            new_node = SinglyLinkedListNode( cur_1.data )

            # cur_1 move forward
            cur_1 = cur_1.next
        else:
            new_node = SinglyLinkedListNode( cur_2.data )

            # cur_2 move forward
            cur_2 = cur_2.next

        # add into merger linked list
        merge_point.next = new_node

        # merge_point move forward
        merge_point = merge_point.next



    # linked list 1 is empty, dump linked list 2 into merger linked list
    while cur_2 is not None:
        new_node = SinglyLinkedListNode( cur_2.data )

        # cur_2 move forward
        cur_2 = cur_2.next

        # add into merger linked list
        merge_point.next = new_node

        # merge_point move forward
        merge_point = merge_point.next


    # linked list 2 is empty, dump linked list 1 into merger linked list
    while cur_1 is not None:
        new_node = SinglyLinkedListNode( cur_1.data )

        # cur_1 move forward
        cur_1 = cur_1.next

        # add into merger linked list
        merge_point.next = new_node

        # merge_point move forward
        merge_point = merge_point.next


    # read head node of merged linked list = next of dummy head node
    real_head = head_of_merge.next

    return real_head



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
