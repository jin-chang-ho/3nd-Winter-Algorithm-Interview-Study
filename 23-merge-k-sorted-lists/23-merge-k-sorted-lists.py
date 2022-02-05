# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        value = []
        
        for li in lists:
            l = li
            while l is not None:
                value.append(l.val)
                l = l.next
        
        if not value:
            return None
        
        value.sort()
        
        answer = ListNode(value[0])
        
        head = answer
        
        while len(value) != 1:
            temp_Node = ListNode(value.pop(1))
            answer.next = temp_Node
            answer = answer.next
            
        return head