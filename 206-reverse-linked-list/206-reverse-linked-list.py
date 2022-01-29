# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        answer = Optional[ListNode]
        chase_list = []
        
        while head != None:
            chase_list.append(head.val)
            head = head.next
        
        chase_list.reverse()
        
        answer = ListNode(chase_list[0])
        
        answer_head = answer
        
        for chase in chase_list[1:]:
            answer.next = ListNode(chase)
            answer = answer.next
            
        return answer_head
        
            