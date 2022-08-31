# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = None
        c = head
        while c!=None:
            n = c.next
            c.next = p
            p = c
            c = n
        return p
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def fun(head, prev):
            if head == None:
                return prev
            next = head.next
            head.next = prev
            return fun(next, head)
        return fun(head, None)