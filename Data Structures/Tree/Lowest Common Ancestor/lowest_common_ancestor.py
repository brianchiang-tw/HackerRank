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





'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
  #Enter your code here


    if root is None:
        # corner case: empty tree
        return None
    
    if root.info == v1 or root.info == v2:
        # corner case: either v1 or v2 is root of tree
        return root

    # ancestor of left subtree
    left_ancestor = lca( root.left, v1, v2 )

    # ancestor of right subtree
    right_ancestor = lca( root.right, v1, v2 )


    if left_ancestor is not None and right_ancestor is not None:
        # ancestors belong to two different side, root is the Lowest Common Ancestor
        return root

    
    if left_ancestor is not None:
        # ancestors belong to left sub-tree, left_ancestor is the Lowest Common Ancestor
        return left_ancestor

    else:
        # ancestors belong to right sub-tree, right_ancestor is the Lowest Common Ancestor
        return right_ancestor





tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
