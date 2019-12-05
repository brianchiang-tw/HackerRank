class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.

        # create a new node with given value
        new_node = Node( val )

        insert_position = self.root

        parent = insert_position

        if self.root is None:
            #print("insert at root")
            self.root = new_node
            return self.root
        else:

            direction = None
            
            while( insert_position is not None ):

                parent = insert_position

                if val > insert_position.info:
                    
                    direction = "right"

                    # if val is larger than current, go right
                    insert_position = insert_position.right

                else:
                    direction = "left"

                    # if val is smaller than current, go left
                    insert_position = insert_position.left


            if direction == "right":
                parent.right = new_node
            elif direction == "left":
                parent.left = new_node 
            
            return self.root


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
