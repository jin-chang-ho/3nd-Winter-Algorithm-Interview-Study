# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum_number = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def check(node):
            if node == None:
                return 0
            
            right = check(node.right)
            
            self.sum_number += node.val
            node.val = self.sum_number
            
            left = check(node.left)
            
            return 0
            
            
        check(root)
        
        return root
        