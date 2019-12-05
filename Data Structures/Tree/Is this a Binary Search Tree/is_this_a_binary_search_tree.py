""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_bst_with_bound(root, min, max):

    # empty node or empty tree
    if root is None:
        return True
    
    # if the value of node is out of bound
    if root.data < min or root.data > max:
        # each node in BST must be within (min, max)
        return False
    
    # check left sub-tree
    is_left_bst = check_bst_with_bound(root.left, min, root.data-1 )
    
    # check right sub-tree
    is_right_bst = check_bst_with_bound(root.right, root.data+1, max )
    return (is_left_bst and is_right_bst)
    

def check_binary_search_tree_(root):
    
    is_bst = check_bst_with_bound( root, min = -1, max = 10001) 
    
    return is_bst
        