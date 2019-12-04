def reverse(head):

    if head is None:
        return head
    if head.next is None and head.prev is None:
        return head


    cur = head
    next_1 = cur.next
    next_2 = next_1.next

    while( next_1 is not None ):

        # reverse linkage direction
        cur.prev = next_1
        next_1.next = cur

        # corner case for head node
        if cur is head:
            cur.next = None

        # cur, next_1 move forward
        cur = next_1
        next_1 = next_2

        if next_2 is not None:

            # next_2 move forward
            next_2 = next_2.next

        else:
            # update tail node as new head of reversed linked list
            head = cur

            # update new head's prev to None
            head.prev = None

            # whole reverse process is accomplisged, return new head
            return head