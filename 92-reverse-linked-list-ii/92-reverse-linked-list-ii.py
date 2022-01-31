# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        answer = head
        
        for _ in range(left - 1):
            if not head:
                return answer
            head = head.next
            
        reverse_list = []
        
        for _ in range(left, right + 1):
            if not head:
                return answer
            reverse_list.append(head.val)
            head = head.next
            
        reverse_list.reverse()
        
        head = answer
        
        for _ in range(left - 1):
            head = head.next
            
        for _ in range(left, right + 1):
            head.val = reverse_list.pop(0)
            head = head.next
        
        return answer