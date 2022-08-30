# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def fun(root, low, high, sum):
            if root == None:
                return sum
            if root.val >= low and root.val <= high:
                sum+=root.val
            sum = fun(root.left, low, high, sum)
            sum = fun(root.right, low, high, sum)
            return sum
        return fun(root, low, high, 0)
class Solution1:
    sum = 0 
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def fun(root, low, high):
            if root == None:
                return
            if root.val >= low and root.val <= high:
                self.sum+=root.val
            fun(root.left, low, high)
            fun(root.right, low, high)
            return self.sum
        return fun(root, low, high)