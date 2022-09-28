# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head==None:
            return head
        l = 0
        temp = head
        while temp!=None:
            l+=1
            temp = temp.next
        pos = l-n+1
        if l==1 and pos==1:
            return None
        count = 1
        temp = head
        if pos==1:
            head = temp.next
            return head
        while count < pos and temp.next!=None:
            prev = temp
            temp = temp.next
            count+=1
        prev.next = temp.next
        return head
        