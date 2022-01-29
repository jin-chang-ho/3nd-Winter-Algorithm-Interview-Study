# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_number = []
        l2_number = []
        
        if l1 == None and l2 == None:
            return None
        
        if l1 == None:
            return l2
        
        if l2 == None:
            return l1
        
        while l1 != None:
            l1_number.append(str(l1.val))
            l1 = l1.next
            
        while l2 != None:
            l2_number.append(str(l2.val))
            l2 = l2.next 
            
        l1_number.reverse()
        l2_number.reverse()
        
        l1_number = int("".join(l1_number))
        l2_number = int("".join(l2_number))
        
        answer_number = l1_number + l2_number
        
        if answer_number == 0:
            return ListNode(0)
        
        answer_list = []
        
        while answer_number != 0:
            answer_list.append(answer_number % 10)
            answer_number = answer_number // 10
        
        answer = Optional[ListNode]
        
        answer = ListNode(answer_list[0])
        
        head = answer
        
        for ans in answer_list[1:]:
            answer.next = ListNode(ans)
            answer = answer.next
            
        return head
            
        