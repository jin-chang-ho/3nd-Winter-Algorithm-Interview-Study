# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == []:
            return False
        
        vals = [head.val]
        chase_next = head.next
        
        while chase_next != None:
            vals.append(chase_next.val)
            chase_next = chase_next.next
        
        start, end = 0, len(vals) - 1
        
        while end - start >= 1:
            if vals[start] != vals[end]:
                return False
            start = start + 1
            end = end - 1
        
        return True
            