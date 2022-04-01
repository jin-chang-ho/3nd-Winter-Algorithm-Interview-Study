# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    depth = 0
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node == None:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.depth = max(self.depth, abs(left - right))
            
            return max(left, right) + 1
        
        dfs(root)
        
        if self.depth >= 2:
            return False
        
        return True