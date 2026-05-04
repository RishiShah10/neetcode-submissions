# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Go through the two lists
        check which is bigger 
        copy the pointer going through original
        change pointer to next
        change the copys next to the next list
        """
        head = ListNode()
        point = head
        t1,t2 = list1,list2
        while t1 is not None and t2 is not None:
            if t1.val < t2.val:
                temp = t1.next
                point.next = t1
                t1 = temp
            else:
                #t2.val < t1.val
                temp = t2.next
                point.next = t2
                t2 = temp
            point = point.next
        if t1 is None:
            point.next = t2
        else:
            point.next = t1
        return head.next