#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):

    cur = head

    # create a new node with data
    new_node = DoublyLinkedListNode(data)

    # corner case:
    if head is None:
        # if linked list is empty, update new_node as head of linked list
        head = new_node
        return head






    if data < cur.data:

        # insert new_node at head

        # create double linkage between new_node and cur
        new_node.next = cur
        cur.prev = new_node

        # update new_node as head of linked list
        head = new_node

        return head



    while cur is not None:

        if data >= cur.data:

            if cur.next is not None and data < (cur.next).data :

                # insert new_node in middle

                next_of_new_node = cur.next

                # create double link betwen new_node and next_of_new_node
                new_node.next = next_of_new_node
                next_of_new_node.prev = new_node

                # create double link between new_node and cur
                cur.next = new_node
                new_node.prev = cur

                return head
            elif cur.next is None:
                # insert new_node at tail

                # create double link between new_node and cur
                cur.next = new_node
                new_node.prev = cur

                return head

        # cur mve forward
        cur = cur.next



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
