# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        t = head
        h = head.next
        while h and h.next is not None:
            if t == h:
                return True
            t = t.next
            h = h.next.next
        return False
            


        