# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer = Optional[ListNode]
        
        if list1 == None and list2 == None:
            return None
        
        if list1 == None:
            return list2
        
        if list2 == None:
            return list1
        
        if list1.val >= list2.val:
            answer = ListNode(list2.val)
            list2 = list2.next
        else:
            answer = ListNode(list1.val)
            list1 = list1.next
        
        head = answer
        
        while list1 != None and list2 != None:
            print(list1.val, list2.val)
            if list1.val >= list2.val:
                answer.next = ListNode(list2.val)
                answer = answer.next
                list2 = list2.next
            else:
                answer.next = ListNode(list1.val)
                answer = answer.next
                list1 = list1.next
                
        while list1 != None:
            answer.next = ListNode(list1.val)
            answer = answer.next
            list1 = list1.next
            
        while list2 != None:
            answer.next = ListNode(list2.val)
            answer = answer.next
            list2 = list2.next
            
        return head
        
        