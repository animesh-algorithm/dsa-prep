class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root.left == None or root.right == None:
            return root.val
        return root.val == self.checkTree(root.left)+self.checkTree(root.right)