class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

def static_var(varname, value):
    def decorate(func):
        setattr(func, varname, value)
        return func
    return decorate


@static_var("root_of_tree", None)
def postOrder(root):
    #Write your code here

    if postOrder.root_of_tree is None:
        postOrder.root_of_tree = root

    if root is not None:

        # recursive definition of post order
        #   visit root.left 
        #   visit root.right
        #   visit root.right

        postOrder( root.left )

        postOrder( root.right )

        if root is not postOrder.root_of_tree:
            print( root.info, end = ' ')
        else:
            print( root.info, end = '')



