# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val_list = []
        chase = head
        
        while chase is not None:
            val_list.append(chase.val)
            chase = chase.next
            
        val_list.sort()
        
        chase = head
        
        while chase is not None:
            chase.val = val_list.pop(0)
            chase = chase.next
            
        return head