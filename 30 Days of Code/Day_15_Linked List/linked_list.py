class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method

        # create a new node with data
        new_node = Node(data)

        if head is None:
            # empty linked list
            head = new_node

        else:
            # non-empty linked list
            current = head

            # moveing to insert position
            while current.next is not None:
                current = current.next

            current.next = new_node
        
        return head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  