# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum_value = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if node == None:
                return
        
            dfs(node.left)
            dfs(node.right)
            
            if node.val >= low and node.val <= high:
                self.sum_value += node.val
        
        dfs(root)
        return self.sum_value