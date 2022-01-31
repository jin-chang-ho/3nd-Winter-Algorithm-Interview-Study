# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = head
        
        while (head is not None) and (head.next is not None):   
            next_node = head.next
            head.val, next_node.val = next_node.val, head.val
            head = head.next.next
            
        return answer
            