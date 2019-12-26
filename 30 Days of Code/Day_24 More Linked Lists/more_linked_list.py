class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        cur = head
        next_node = cur.next

        while cur is not None:

            while next_node and next_node.data == cur.data:

                new_next_of_cur = next_node.next

                # update cur's next to next two element
                cur.next = new_next_of_cur

                # update next_node
                next_node = cur.next
            
            # cur keeps moving forward
            cur = cur.next

            if cur :
                # update next_node
                next_node = cur.next

        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 