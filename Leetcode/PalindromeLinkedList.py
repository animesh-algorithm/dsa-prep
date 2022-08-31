# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []
        while head!=None:
            res.append(head.val)
            head = head.next
        i=0
        while i<=len(res)//2:
            if res[i]!=res.pop():
                return False
            i+=1
        return True