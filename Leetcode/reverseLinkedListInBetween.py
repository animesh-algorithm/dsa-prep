# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def fun(curr, prev, end):
            if prev==end or curr==None:
                return end
            next = curr.next
            curr.next = prev
            return fun(next, curr, end)
        count = 1
        curr = head
        start = None
        prevOfStart = None
        prev = None
        while curr != None:
            if count == left:
                prevOfStart=prev
                start = curr
            if count == right:
                end = curr
                break
            prev = curr
            curr = curr.next
            count+=1
        next = start.next
        start.next = end.next
        end = fun(next, start, end)
        if prevOfStart:
            prevOfStart.next = end
        else:
            head = end
        return head