# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        odd_deque: Deque = collections.deque()
        even_deque: Deque = collections.deque()
    
        answer = head
        head = head.next
        count = 1
        
        while head is not None:
            if count % 2 != 0:
                odd_deque.append(head.val)
            else:
                even_deque.append(head.val)
            
            head = head.next
            count = count + 1
            
        head = answer.next
        
        for i in range(len(even_deque)):
            head.val = even_deque[i]
            head = head.next
            
        for i in range(len(odd_deque)):
            head.val = odd_deque[i]
            head = head.next
            
        return answer
            
        