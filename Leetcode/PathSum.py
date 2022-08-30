# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def solve(root, target, sum):
            if not root:
                return False

            sum+=root.val
            if not root.left and not root.right:
                return sum==target
            return solve(root.left, target, sum) or solve(root.right, target, sum)
        return solve(root, targetSum, 0) if root else False