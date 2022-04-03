# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def make(chase):
            if chase == []:
                return None
            index = len(chase) // 2
            node = TreeNode(chase[index])
            node.left = make(chase[:index])
            node.right = make(chase[index + 1:])
            
            return node
            
        return make(nums)
        