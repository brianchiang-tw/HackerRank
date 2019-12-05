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

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def static_var( varname, value):
    def decorate( func):
        setattr( func, varname, value)
        return func
    
    return decorate


@static_var("root_of_tree", None)
def height(root):

    if height.root_of_tree is None:
        height.root_of_tree = root

    if root is None:
        return 0

    else:
        height_of_cur = 1 + max( height(root.left), height(root.right) )
        #print( "cur = {} with h = {}".format( root.info, height_of_cur) )

        if root is height.root_of_tree:
            return height_of_cur-1
        else:
            return (height_of_cur)


