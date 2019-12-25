import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root


    def levelOrder(self,root):
        
        from collections import deque

        bfs_queue = deque( [ (root, 1) ] )
        traversal = []

        while bfs_queue:
        
            cur_node, cur_level = bfs_queue.popleft()

            if cur_node:
                # non-empty node
                traversal.append( str(cur_node.data) )
            else:
                # empty node
                continue

            # enqueue left child
            bfs_queue.append( (cur_node.left, cur_level+1) )

            # enqueue right child
            bfs_queue.append( (cur_node.right, cur_level+1) )


        output_str =  ' '.join( traversal )
        print( output_str )


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
